"""Salin gambar front-page entri ke direktori output dan verifikasi salinannya.

Program ini hanya menyalin satu berkas, ``entry.png``, yang berada di folder
yang sama dengan skrip ini, ke direktori output. Nama berkas hasil salinan
tetap ``entry.png``. Setelah menyalin, program menghitung hash SHA-256 penuh
dari berkas sumber dan dari salinan, lalu membandingkannya untuk memastikan
salinan byte-identik dengan sumbernya.

Direktori output diambil dari variabel lingkungan ``MAKEFUN_OUTPUT_DIR`` bila
disetel; bila tidak, dipakai ``/output``. Bila direktori output sama dengan
folder sumber, tidak ada penyalinan yang perlu dilakukan: program cukup
memverifikasi berkas yang sudah ada di tempatnya dan selesai dengan sukses.

Hanya memakai pustaka standar Python; tidak ada akses jaringan.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path


SOURCE_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"


def sha256_of(path):
    """Hitung hash SHA-256 penuh dari sebuah berkas, dibaca per blok."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        while True:
            block = handle.read(1024 * 1024)
            if not block:
                break
            digest.update(block)
    return digest.hexdigest()


def resolve_output_dir():
    """Tentukan direktori output dari lingkungan, atau pakai bawaan."""
    configured = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if configured:
        return Path(configured)
    return Path(DEFAULT_OUTPUT_DIR)


def main():
    script_dir = Path(__file__).resolve().parent
    source = script_dir / SOURCE_NAME

    if not source.is_file():
        print(f"error: sumber tidak ditemukan: {source}", file=sys.stderr)
        return 1

    output_dir = resolve_output_dir()
    destination = output_dir / SOURCE_NAME

    source_hash = sha256_of(source)
    print(f"sumber: {source}")
    print(f"sha256 sumber: {source_hash}")

    if output_dir.resolve() == script_dir.resolve() or (
        destination.exists() and destination.resolve() == source.resolve()
    ):
        print("tujuan sama dengan sumber; "
              "tidak ada penyalinan, berkas sudah di tempatnya.")
        print(f"sha256 terverifikasi: {source_hash}")
        print("selesai: OK")
        return 0

    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)

    copied_hash = sha256_of(destination)
    print(f"salinan: {destination}")
    print(f"sha256 salinan: {copied_hash}")

    if copied_hash != source_hash:
        print("error: hash salinan tidak cocok dengan sumber", file=sys.stderr)
        return 1

    print("verifikasi: salinan byte-identik dengan sumber")
    print("selesai: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
