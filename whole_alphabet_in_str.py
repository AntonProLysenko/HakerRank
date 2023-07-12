def pangrams(s):
    # Write your code here
    s_arr = list(s.lower())
    for i in (s_arr):
        if i == " ":
            s_arr.remove(i)
   
    s_arr.sort()
    set_arr = set(s_arr) 
    if len(set_arr) < 26:
        return("not pangram")
    else:
        return("pangram")
    
test = "CSeBBZvYvDyayyBzdfdXvaBtxxwiXcD jQADzTCXzBxzwcyxbd cdyxcBbcxsVD wzXXzazCeqYyB CZzXyxAb WX zbtAdxRVyWEAB DbdAd ViYxzCSAuCVZVXyZY gfWzczBaAZWzXwy AXyXRvyrRZHxtedwcbAWeYiA ZwBea tQZaTXCoWbE cbtZvWZAziwA BWzBaVGbz yyECVAdAcSizBWgGTBz i BEJDELZ WBbaAEOGwbBcZZAvrYDmCWhT WycaXTatCwzavAwewZAZZWb ezBywzdYBhbZeVZBEZFuiPBafxyYzAdDxBb BcidxCV c oDZxgfbycygBdx y dCY ZEEZ txzasvxZADzcDzxhZzXBbDdaobzDYIwyAcXDdthWW U cjfzVWaCecAzaZzaAAUFXgcCYAZzD zABU CcaVZCZ Z xayFyXYAYyGavzVyZyzBe AxYzaACI hxXAaB UayBY y fCz ByXW AwxZzchzAwSwVBzuCW WaeddADAZycwa vZTjd czdWyzaybBeTCXYYZcBZtGy aSZrBAcZwcY BAcAeDFaA aXBhFwAyC IeW Y CaA AbWtSFbzVZIxTACZAaBYIBxbBAzCdAaWaWaAxAcvZaZZTzBBZZsug YtaYtmdxBzFDDzWWHhacAZDuzVyDBADAYaaxAqraXUzzJAAEAZSCWAbYZZyUfAyWYBKEZca bdbQazBEBXD XAdLwWHwwxFaFXxVZZyzcykCwcwaScqyDvB wAxdbDAZXFeEcwWbvbhFHxbYWAYab bZFzBIdax XvC ZcD DZxzabAcYavbdyFRBBbZWuu vzQAvZAVWAYSYbbCZfZWBXWeAZsXBcbaZfEbgEAIZvyCBwEydWa JByZedADvCZyftcUexYbYca BvZBCcybXbz zBUXdye zy YDaYEcAzdeaqEy ZDVSd dacbS szuzZSH ADycXCUDVb"
print(pangrams(test))