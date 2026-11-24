#!/usr/bin/env python3
"""Salin entry.png ke direktori output lalu verifikasi salinannya.

Program ini menyalin gambar front-page (entry.png) yang terletak di folder
yang sama dengan script ini ke sebuah direktori output, kemudian memastikan
salinan tersebut identik byte demi byte dengan membandingkan hash SHA-256
penuh dari sumber dan salinan.

Direktori output diambil dari variabel lingkungan MAKEFUN_OUTPUT_DIR bila
disetel; bila tidak, dipakai /output. Nama file output selalu entry.png.

Bila direktori output ternyata sama dengan folder sumber, tidak ada
penyalinan yang dilakukan: file yang sudah ada di tempatnya cukup
diverifikasi hash-nya, lalu program selesai dengan sukses.

Hanya memakai Python stdlib dan tidak memakai network sama sekali.
"""

import hashlib
import os
import shutil
import sys

SOURCE_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"


def sha256_of(path):
    """Hitung hash SHA-256 penuh dari sebuah file, dibaca per blok."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        while True:
            block = handle.read(1024 * 1024)
            if not block:
                break
            digest.update(block)
    return digest.hexdigest()


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(script_dir, SOURCE_NAME)

    if not os.path.isfile(source_path):
        print(f"error: sumber tidak ditemukan: {source_path}", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    # realpath (bukan abspath) supaya folder yang sama tapi diakses lewat
    # symlink atau alias path tetap terdeteksi sebagai folder sumber, karena
    # menyalin file ke dirinya sendiri akan crash di shutil.copyfile.
    output_dir = os.path.realpath(output_dir)
    destination_path = os.path.join(output_dir, SOURCE_NAME)

    source_hash = sha256_of(source_path)

    if os.path.realpath(script_dir) == output_dir:
        print(f"output sama dengan folder sumber; memverifikasi {source_path}")
        print(f"sha256: {source_hash}")
        print("ok: file sudah berada di tempatnya dan terverifikasi")
        return 0

    os.makedirs(output_dir, exist_ok=True)
    shutil.copyfile(source_path, destination_path)

    copy_hash = sha256_of(destination_path)
    print(f"sumber : {source_path} ({source_hash})")
    print(f"salinan: {destination_path} ({copy_hash})")

    if copy_hash != source_hash:
        print("error: hash salinan tidak cocok dengan sumber", file=sys.stderr)
        return 1

    print("ok: salinan byte-identik dengan sumber")
    return 0


if __name__ == "__main__":
    sys.exit(main())
