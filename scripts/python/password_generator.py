#!/usr/bin/env python3
"""
Générateur de mots de passe sécurisés pour le collectif Indignons-nous
Génère des mots de passe forts avec différents niveaux de sécurité
"""

import random
import string
import secrets
import argparse

def generate_password(length=12, use_symbols=True, use_numbers=True, use_uppercase=True):
    """Génère un mot de passe sécurisé"""
    
    # Base : lettres minuscules
    chars = string.ascii_lowercase
    
    # Ajout conditionnel des caractères
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Génération sécurisée
    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password

def generate_passphrase(words=4):
    """Génère une phrase de passe mémorable"""
    word_list = [
        'indignons', 'collectif', 'revolution', 'liberte', 'justice',
        'solidaire', 'ensemble', 'changement', 'avenir', 'espoir',
        'action', 'mouvement', 'unite', 'force', 'courage',
        'digital', 'secure', 'crypto', 'privacy', 'freedom'
    ]
    
    selected_words = [secrets.choice(word_list) for _ in range(words)]
    # Capitaliser aléatoirement et ajouter des chiffres
    passphrase = []
    for word in selected_words:
        if secrets.randbelow(2):
            word = word.capitalize()
        passphrase.append(word)
    
    # Ajouter des chiffres aléatoires
    passphrase.append(str(secrets.randbelow(1000)))
    
    return '-'.join(passphrase)

def check_strength(password):
    """Évalue la force d'un mot de passe"""
    score = 0
    feedback = []
    
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Trop court (min 8 caractères)")
    
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        score += 2
    
    if score >= 6:
        strength = "🔒 TRÈS FORT"
    elif score >= 4:
        strength = "🔐 FORT"
    elif score >= 2:
        strength = "⚠️  MOYEN"
    else:
        strength = "❌ FAIBLE"
    
    return strength, score, feedback

def main():
    parser = argparse.ArgumentParser(description='Générateur de mots de passe sécurisés')
    parser.add_argument('-l', '--length', type=int, default=12, help='Longueur du mot de passe')
    parser.add_argument('-n', '--count', type=int, default=1, help='Nombre de mots de passe')
    parser.add_argument('--no-symbols', action='store_true', help='Sans symboles')
    parser.add_argument('--no-numbers', action='store_true', help='Sans chiffres')
    parser.add_argument('--no-uppercase', action='store_true', help='Sans majuscules')
    parser.add_argument('-p', '--passphrase', action='store_true', help='Générer une phrase de passe')
    
    args = parser.parse_args()
    
    print("🔐 Générateur de mots de passe - Collectif Indignons-nous")
    print("=" * 60)
    
    for i in range(args.count):
        if args.passphrase:
            password = generate_passphrase()
            print(f"\n📝 Phrase de passe {i+1}: {password}")
        else:
            password = generate_password(
                length=args.length,
                use_symbols=not args.no_symbols,
                use_numbers=not args.no_numbers,
                use_uppercase=not args.no_uppercase
            )
            print(f"\n🔑 Mot de passe {i+1}: {password}")
        
        strength, score, feedback = check_strength(password)
        print(f"   Force: {strength} (Score: {score}/8)")
        
        if feedback:
            print(f"   Conseils: {', '.join(feedback)}")
    
    print(f"\n💡 Conseil: Utilisez un gestionnaire de mots de passe !")

if __name__ == "__main__":
    main()