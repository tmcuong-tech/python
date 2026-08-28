"""Python has many ways to format strings!"""

# f-strings
domain = "github.com"
url = f"https://{domain}/"
print(url)

tlist = ["one", "two", "three"]
print(f"There are {len(tlist)} item(s) in tlist.")

tlen = len(tlist)
print(
    f"There {"is" if tlen == 1 else "are"} {tlen} item{"" if len(tlist) == 1 else "s"} in tlist."
)

# format()
domain = "redhat.com"
url = "https://{}/".format(domain)
print(url)

protocol = "https"
domain = "github.com"
path = "jacobcallahan"

url1 = "{}://{}/{}".format(protocol, domain, path)
url2 = "{1}://{2}/{0}".format(path, protocol, domain)
url3 = "{proto}://{dom}/{pth}".format(proto=protocol, dom=domain, pth=path)
print(url1)
print(url2)
print(url3)

full_details = {
    "owner": {
        "display_name": "Earnest P. Worrell",
        "email_address": "earnest.worrel@realmail.com",
    }
}
owner1 = f"{full_details['owner']['display_name']} <{full_details['owner']['email_address']}>"

owner2 = "{display_name} <{email_address}>".format(
    display_name=full_details["owner"]["display_name"],
    email_address=full_details["owner"]["email_address"],
)
print(owner1)
print(owner2)

# % formatting

name = "James"
age = 35
occupation = "Engineer"

person = "Name: %s, Age: %d, Occupation: %s" % (name, age, occupation)
print(person)
