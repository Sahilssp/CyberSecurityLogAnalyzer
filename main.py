from collections import Counter

failed_ips = []

with open("sample_log.txt", "r") as file:
    for line in file:

        if "Failed login" in line:

            ip = line.split("from")[1].strip()
            failed_ips.append(ip)

print("===== Security Report =====")

print("Total Failed Logins:", len(failed_ips))

ip_count = Counter(failed_ips)

print("\nSuspicious IP Addresses:")

for ip, count in ip_count.items():
    print(ip, "->", count, "attempts")
print("\n===== Risk Assessment =====")

if len(failed_ips) >= 5:
    print("Risk Level: HIGH")
elif len(failed_ips) >= 3:
    print("Risk Level: MEDIUM")
else:
    print("Risk Level: LOW")
print("\n===== Brute Force Detection =====")

for ip, count in ip_count.items():

    if count >= 2:
        print("ALERT:", ip, "may be performing a brute force attack")