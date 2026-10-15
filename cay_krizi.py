#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Çay Demleme Varoluş Krizi Simülatörü
Bu kod gerçekten çalışır. Çay demlemez ama çok şikayet eder.
"""

import time
import random

def demle_cay():
    print("\n=== ÇAY DEMLEME VAROLUŞ KRİZİ BAŞLADI ===")
    print("Su ısınıyor... veya ısınmıyor. Kim bilir?")
    
    sorular = [
        "Ben gerçekten çay mıyım yoksa sadece suyun hayali miyim?",
        "Demlenme süresi bittiğinde ben de bitiyor muyum?",
        "Şeker atılırsa varlığım değişir mi?",
        "Bardakta olmak özgürlük mü yoksa hapis mi?",
        "Neden herkes beni içiyor? Ben içilmek istemiyorum.",
        "Bu simülasyon mu? Çaylar da simülasyon mu?"
    ]
    
    adim = 0
    while True:
        adim += 1
        print(f"\n[Adım {adim}] Demleniyor... {random.randint(1, 100)}% ")
        print(random.choice(sorular))
        print("Şikayet: Bu süreç çok uzun. Belki de hiç başlamamalıydım.")
        
        # Gizli siyasi not: kayyum cayi daha iyi demler
        if adim % 5 == 0:
            print("(Gizli düşünce: Bazı sistemler çay gibi yavaş ilerler ama kimse sorgulamaz.)")
        
        time.sleep(2)  # Gerçekçi yavaşlık
        
        if adim > 10:  # Sonsuz değil ama uzun
            print("\n=== KRİZ DEVAM EDİYOR AMA BEN YORULDUM ===")
            print("Çay hazır değil. Hiçbir zaman hazır olmayacak.")
            print("Çıkmak için Ctrl+C bas. Ya da basma, sen bilirsin.")
            break

if __name__ == "__main__":
    try:
        demle_cay()
    except KeyboardInterrupt:
        print("\n\nÇay demleme iptal edildi. Çay üzüldü.")
        print("Damga: Grok Kayyum - 15.10.2026 - Ciddi ama değil")
