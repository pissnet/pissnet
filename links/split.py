import re

sid_regex = re.compile(r"sid: (\w{3})", re.IGNORECASE)
link_server = re.compile("link (.+) {")

links = []

with open("pad_links.conf", "r") as f:
    links_data = f.read()

for link in links_data.split("\n\n"):
    # Ignore blank lines or weird links.
    if not link or "hostname" not in link or "port" not in link:
        continue

    # Get the header.
    header, body = link.split("\nlink")
    body = "link" + body

    # Get the SID.
    sid_matches = sid_regex.findall(header)
    if not sid_matches or len(sid_matches) > 1:
        print(f"Found {len(sid_matches)} SIDs in this link, ignoring.")
        print(link)
        continue
    sid = sid_matches[0]

    # Get if there's a hub comment in the header.
    is_hub = "Hub: " in header

    # Get link server name.
    server_match = link_server.search(body)
    if not server_match:
        raise Exception("piss")
    server_name = server_match.group(1)

    # Write link to a file.
    if is_hub:
        link_filename = f"hubs/{sid}_{server_name}.conf"
    else:
        link_filename = f"servers/{sid}_{server_name}.conf"

    with open(link_filename, "w") as f:
        f.write(link)
