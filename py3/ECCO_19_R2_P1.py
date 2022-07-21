for x in range(10):
    n = int(input())
    uniqueAddresses = 0
    addresses = []
    for t in range(n):
        address = input().split("@")
        newAd = ""
        for letter in address[0]:
            if letter == ".":
                continue
            elif letter == "+":
                break
            newAd += letter
        newAd += "@" + address[1]
        newAd = newAd.lower()
        if newAd not in addresses:
            uniqueAddresses += 1
            addresses.append(newAd)

    print(uniqueAddresses)
