#!/usr/bin/env python3
"""
Nettoyage automatique des projets de développement
Supprime les fichiers temporaires, caches, logs inutiles
"""

import os
import shutil
import glob

def clean_project():
    """Nettoie les fichiers temporaires du projet"""
    patterns = [
        '**/__pycache__',
        '**/*.pyc', 
        '**/.pytest_cache',
        '**/node_modules',
        '**/.DS_Store',
        '**/Thumbs.db',
        '**/*.log',
        '**/.vscode/settings.json',
        '**/dist',
        '**/build'
    ]
    
    cleaned = []
    for pattern in patterns:
        for path in glob.glob(pattern, recursive=True):
            try:
                if os.path.isdir(path):
                    shutil.rmtree(path)
                else:
                    os.remove(path)
                cleaned.append(path)
            except:
                pass
    
    print(f"✅ {len(cleaned)} fichiers/dossiers nettoyés")
    return cleaned

if __name__ == "__main__":
    clean_project()