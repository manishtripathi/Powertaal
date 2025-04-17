#!/usr/bin/env python
import os
import sys
import polib
import glob

def compile_po_files():
    """Compile all .po files to .mo files."""
    locale_dir = os.path.join(os.path.dirname(__file__), 'locale')
    
    if not os.path.exists(locale_dir):
        print(f"Error: Locale directory {locale_dir} does not exist.")
        return
    
    po_files = glob.glob(os.path.join(locale_dir, '*', 'LC_MESSAGES', '*.po'))
    
    if not po_files:
        print("No .po files found to compile.")
        return
    
    for po_file in po_files:
        mo_file = po_file.replace('.po', '.mo')
        try:
            po = polib.pofile(po_file)
            po.save_as_mofile(mo_file)
            print(f"Compiled {po_file} to {mo_file}")
        except Exception as e:
            print(f"Error compiling {po_file}: {e}")

if __name__ == '__main__':
    try:
        import polib
    except ImportError:
        print("Error: polib is not installed. Please install it with 'pip install polib'.")
        sys.exit(1)
    
    compile_po_files() 