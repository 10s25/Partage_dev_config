#!/bin/bash

# Script de purge simple avec gh CLI
set -e

OWNER="10s25"
REPO="Partage_dev_config"

echo "🚀 Purge simple des actions GitHub"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Vérifier gh CLI
if ! gh auth status &> /dev/null; then
    echo "❌ GitHub CLI pas authentifié. Lancez: gh auth login"
    exit 1
fi

echo "✅ GitHub CLI authentifié"

# Lister les runs
echo "📋 Liste des workflow runs:"
gh run list --repo $OWNER/$REPO --limit 20

echo ""
read -p "⚠️  Voulez-vous supprimer TOUS les runs? (y/N): " -n 1 -r
echo

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Opération annulée"
    exit 0
fi

echo "🗑️  Suppression en cours..."

# Méthode alternative: supprimer un par un avec confirmation automatique
gh run list --repo $OWNER/$REPO --limit 100 --json databaseId --jq '.[].databaseId' | while read -r run_id; do
    if [ -n "$run_id" ] && [ "$run_id" != "null" ]; then
        echo -n "   Suppression du run $run_id... "
        
        # Utiliser l'API directement
        if gh api -X DELETE "repos/$OWNER/$REPO/actions/runs/$run_id" 2>/dev/null; then
            echo "✅"
        else
            echo "❌"
        fi
        
        sleep 0.2
    fi
done

echo ""
echo "✅ Purge terminée!"
echo "🎉 Vérifiez sur: https://github.com/$OWNER/$REPO/actions"