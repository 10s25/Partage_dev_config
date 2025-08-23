#!/usr/bin/env python3
"""
Monitoring système en temps réel
Surveille CPU, RAM, disque pour les serveurs du collectif
"""

import psutil
import json
import time
from datetime import datetime

def get_system_info():
    """Récupère les infos système"""
    return {
        'timestamp': datetime.now().isoformat(),
        'cpu_percent': psutil.cpu_percent(interval=1),
        'memory': {
            'total': psutil.virtual_memory().total // (1024**3),
            'used': psutil.virtual_memory().used // (1024**3),
            'percent': psutil.virtual_memory().percent
        },
        'disk': {
            'total': psutil.disk_usage('/').total // (1024**3),
            'used': psutil.disk_usage('/').used // (1024**3),
            'percent': psutil.disk_usage('/').percent
        },
        'network': {
            'bytes_sent': psutil.net_io_counters().bytes_sent,
            'bytes_recv': psutil.net_io_counters().bytes_recv
        }
    }

def check_alerts(info):
    """Vérifie les seuils d'alerte"""
    alerts = []
    
    if info['cpu_percent'] > 80:
        alerts.append(f"🔥 CPU élevé: {info['cpu_percent']:.1f}%")
    
    if info['memory']['percent'] > 85:
        alerts.append(f"⚠️ RAM critique: {info['memory']['percent']:.1f}%")
    
    if info['disk']['percent'] > 90:
        alerts.append(f"💾 Disque plein: {info['disk']['percent']:.1f}%")
    
    return alerts

if __name__ == "__main__":
    info = get_system_info()
    alerts = check_alerts(info)
    
    print(json.dumps(info, indent=2))
    
    if alerts:
        print("\n🚨 ALERTES:")
        for alert in alerts:
            print(alert)