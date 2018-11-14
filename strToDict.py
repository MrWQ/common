cookiestr = 'webp=1; __mta=251548217.1540350350647.1540350350647.1540350350647.1; coupon_uuid="AC505AD52F234E83A1831F76F1D2906EQ8qm1GXxT9lhskN3Hs7Tl%2F8aiGR%2BFWmkZZ9qhcel2iAo8ijgQjhbosRYR%2FTmPzAdo5KiK3WoqCcQwlCZgZaVKS0x%2FavFnr52lwHMWCn04%2Fg%3D"; _lxsdk_cuid=166a3e2640ec8-07aba1d3a992fe-8383268-100200-166a3e2640fc8; _lxsdk=166a3e2640ec8-07aba1d3a992fe-8383268-100200-166a3e2640fc8; grap_cookie_phone_ab=13611039986; h_cookie_phone=13611039986; user_coupon_token=49772148; _lx_utm=utm_source%3Dappshare; h_w_uuid=1391a366-5547-4a6f-8922-c3e38dc96bec; ta.uuid=1056119009629679631; isUuidUnion=true; iuuid=166a3e2640ec8-07aba1d3a992fe-8383268-100200-166a3e2640fc8; JSESSIONID=1ffgactt9aqfal45iyqnvqsv7; _lxsdk_s=166c3a57b0c-f85-b4f-f94%7C%7C1'

def strToDict(str):
    cookie = {}
    for line in cookiestr.split(';'):
        key, value = line.split('=', 1)
        cookie[key] = value
    print(cookie)
    return cookie

strToDict(cookiestr)
