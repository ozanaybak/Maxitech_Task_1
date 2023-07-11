from fastapi import FastAPI
import requests
import os

app = FastAPI()

@app.get("/search")
async def search_glassdollar():
    import requests
import json
import asyncio
import aiohttp
import string
import nest_asyncio

nest_asyncio.apply()

cookies = {
    '_ga': 'GA1.2.76544189.1687342534',
    '_ga_SX8XLCG27H': 'GS1.1.1688976373.18.1.1688976384.0.0.0',
    '_gid': 'GA1.2.624975309.1688976109',
    '_gat_gtag_UA_102907215_1': '1',
    'amp_82cffd': 'kBiQKypzW2m50y77l6vUnB...1h4l8511u.1h4l8526i.1.1.2',
    'ph_phc_lnmZRXk93ClxaDiO57RjaSrzVTbSpNZ3Z7ZQQJSIs3M_posthog': '%7B%22distinct_id%22%3A%221892a8284422db-0bdb5abb4196568-3f626b4b-1d03d0-1892a8284436913%22%2C%22%24device_id%22%3A%221892a8284422db-0bdb5abb4196568-3f626b4b-1d03d0-1892a8284436913%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22%24sesid%22%3A%5B1688635345107%2C%221892a828445af-0901201d945bb4-3f626b4b-1d03d0-1892a8284467d90%22%2C1688635343941%5D%2C%22%24session_recording_enabled_server_side%22%3Atrue%2C%22%24console_log_recording_enabled_server_side%22%3Atrue%2C%22%24session_recording_recorder_version_server_side%22%3A%22v1%22%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D',
    '_cc_id': 'd25d20359be494ce8a946969ae893796',
    'panoramaId': '2f1c9d627c3693502d37dbe0a0ae16d53938b935b485fb3d07f73ee5c66cdb42',
    'panoramaIdType': 'panoIndiv',
    'panoramaId_expiry': '1689239949527',
    'euconsent-v2': 'CPttmcAPttmcAAZACBENDJCsAP_AAH_AAAAAJgNX_H__bW9r8f7_aft0eY1P9_j77uQxBhfJk-4F3LvW-JwX52E7NF16tqoKmR4Eu3LBIUNlHNHUTVmwaokVryHsak2cpTNKJ6BEkHMRO2dYCF5vmxtjeQKY5_p_d3fx2D-t_dv-39z3z81Xn3dZf-_0-PCdU5_9Dfn9fRfb-9IP9_78v8v8_9_rk2_eT13_79_7_H9-f_87_BMEAkw1LiALsShwJtAwihRAjCsICKBQAAEAwNEBAA4MCnRGAT6wiQAoBQBGBECHAFGRAIAAAIAkIgAkCLBAAAAIBAACABAIhAAQMAgoALAQCAAEB0DFEKAAQJCBIiIiFMCAiBIICWyoQSgukNMIAqywAoBEbBQAIgABFYAAgLBwDBEgJWLBAlxBtEAAwAIBRKhWoJPTQAKGRssAAAAA.YAAAAAAAAAAA',
    'pubconsent-v2': 'YAAAAAAAAAAA',
    'fpestid': 'zcR1aUPinZxSDu5MufqqO5Iddd9a1Drx-pdJc4S6Lb4VMZqiivUxz7FZLnes_HTgsEKvGg',
}

headers = {
    'Accept': '*/*',
    'Origin': 'https://ranking.glassdollar.com',
    'Accept-Language': 'tr-TR,tr;q=0.9',
    'Host': 'ranking.glassdollar.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Referer': 'https://ranking.glassdollar.com/',
    'Connection': 'keep-alive',
}

search_terms = []

# Single letter terms
for first_letter in string.ascii_lowercase:
    term = first_letter
    search_terms.append(term)

# Single digit terms
for digit in string.digits:
    term = digit
    search_terms.append(term)

# Space character
search_terms.append(" ")

# Two-letter terms
for first_letter in string.ascii_lowercase:
    for second_letter in string.ascii_lowercase:
        term = first_letter + second_letter
        search_terms.append(term)

# Two-letter terms with digits
for first_letter in string.ascii_lowercase:
    for digit in string.digits:
        term = first_letter + digit
        search_terms.append(term)

# Two-letter terms with space character
for first_letter in string.ascii_lowercase:
    term = first_letter + " "
    search_terms.append(term)

# Three-letter terms
for first_letter in string.ascii_lowercase:
    for second_letter in string.ascii_lowercase:
        for third_letter in string.ascii_lowercase:
            term = first_letter + second_letter + third_letter
            search_terms.append(term)

# Three-letter terms with digits
for first_letter in string.ascii_lowercase:
    for second_letter in string.ascii_lowercase:
        for digit in string.digits:
            term = first_letter + second_letter + digit
            search_terms.append(term)

# Three-letter terms with space character
for first_letter in string.ascii_lowercase:
    for second_letter in string.ascii_lowercase:
        term = first_letter + second_letter + " "
        search_terms.append(term)


visited_ids = set()
corporate_ids = []
count = 0  # Counter variable

async def fetch_results(session, term, corporate_ids):
    global count  # Access the global count variable

    json_data = {
        'operationName': 'GIMGetSearchResults',
        'variables': {
            'where': {
                'query': term,
            },
        },
        'query': 'query GIMGetSearchResults($where: searchBarWhere) {\n  searchBar(where: $where)\n}\n',
    }
    response = await session.post('https://ranking.glassdollar.com/graphql', cookies=cookies, headers=headers, json=json_data)

    if response.status == 200:
        response_data = await response.json()
        search_results = response_data['data']['searchBar']

        if search_results:
            for result in search_results['corporates']:
                corporate_id = result['id']
                if corporate_id in visited_ids:
                    continue  # Skip duplicate ID
                visited_ids.add(corporate_id)  # Add ID to visited set
                #print(corporate_id)
                corporate_ids.append(corporate_id)
                # Increase the count
                count += 1
                # Check if count reaches 848
                if count == 848:
                    return
    else:
        print(f"HTTP Error occurred: {response.status} {response.reason}")

# Main function
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        corporate_ids = []  # Create an empty list to store corporate IDs
        for term in search_terms:
            task = asyncio.create_task(fetch_results(session, term, corporate_ids))  # Pass corporate_ids as an argument
            tasks.append(task)
            await asyncio.sleep(0)  # Delay of 0.25 seconds between requests

        await asyncio.gather(*tasks)

        print("All corporate IDs:", corporate_ids)  # Print all the fetched corporate IDs

# Run the main function
asyncio.run(main())


cookies = {
    '_ga': 'GA1.1.76544189.1687342534',
    '_ga_SX8XLCG27H': 'GS1.1.1688731212.16.1.1688732476.0.0.0',
    '_gat_gtag_UA_102907215_1': '1',
    '_gid': 'GA1.2.23330020.1688635129',
    'amp_82cffd': 'kBiQKypzW2m50y77l6vUnB...1h4l8511u.1h4l8526i.1.1.2',
    'ph_phc_lnmZRXk93ClxaDiO57RjaSrzVTbSpNZ3Z7ZQQJSIs3M_posthog': '%7B%22distinct_id%22%3A%221892a8284422db-0bdb5abb4196568-3f626b4b-1d03d0-1892a8284436913%22%2C%22%24device_id%22%3A%221892a8284422db-0bdb5abb4196568-3f626b4b-1d03d0-1892a8284436913%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22%24sesid%22%3A%5B1688635345107%2C%221892a828445af-0901201d945bb4-3f626b4b-1d03d0-1892a8284467d90%22%2C1688635343941%5D%2C%22%24session_recording_enabled_server_side%22%3Atrue%2C%22%24console_log_recording_enabled_server_side%22%3Atrue%2C%22%24session_recording_recorder_version_server_side%22%3A%22v1%22%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D',
    '_cc_id': 'd25d20359be494ce8a946969ae893796',
    'panoramaId': '2f1c9d627c3693502d37dbe0a0ae16d53938b935b485fb3d07f73ee5c66cdb42',
    'panoramaIdType': 'panoIndiv',
    'panoramaId_expiry': '1689239949527',
    'euconsent-v2': 'CPttmcAPttmcAAZACBENDJCsAP_AAH_AAAAAJgNX_H__bW9r8f7_aft0eY1P9_j77uQxBhfJk-4F3LvW-JwX52E7NF16tqoKmR4Eu3LBIUNlHNHUTVmwaokVryHsak2cpTNKJ6BEkHMRO2dYCF5vmxtjeQKY5_p_d3fx2D-t_dv-39z3z81Xn3dZf-_0-PCdU5_9Dfn9fRfb-9IP9_78v8v8_9_rk2_eT13_79_7_H9-f_87_BMEAkw1LiALsShwJtAwihRAjCsICKBQAAEAwNEBAA4MCnRGAT6wiQAoBQBGBECHAFGRAIAAAIAkIgAkCLBAAAAIBAACABAIhAAQMAgoALAQCAAEB0DFEKAAQJCBIiIiFMCAiBIICWyoQSgukNMIAqywAoBEbBQAIgABFYAAgLBwDBEgJWLBAlxBtEAAwAIBRKhWoJPTQAKGRssAAAAA.YAAAAAAAAAAA',
    'pubconsent-v2': 'YAAAAAAAAAAA',
    'fpestid': 'zcR1aUPinZxSDu5MufqqO5Iddd9a1Drx-pdJc4S6Lb4VMZqiivUxz7FZLnes_HTgsEKvGg',
}

headers = {
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Host': 'ranking.glassdollar.com',
    'Accept-Language': 'tr-TR,tr;q=0.9',
    'Origin': 'https://ranking.glassdollar.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Connection': 'keep-alive',
    'Referer': 'https://ranking.glassdollar.com/corporates/8483fc50-b82d-5ffa-5f92-6c72ac4bdaff',
    # 'Content-Length': '522',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_ga=GA1.1.76544189.1687342534; _ga_SX8XLCG27H=GS1.1.1688731212.16.1.1688732476.0.0.0; _gat_gtag_UA_102907215_1=1; _gid=GA1.2.23330020.1688635129; amp_82cffd=kBiQKypzW2m50y77l6vUnB...1h4l8511u.1h4l8526i.1.1.2; ph_phc_lnmZRXk93ClxaDiO57RjaSrzVTbSpNZ3Z7ZQQJSIs3M_posthog=%7B%22distinct_id%22%3A%221892a8284422db-0bdb5abb4196568-3f626b4b-1d03d0-1892a8284436913%22%2C%22%24device_id%22%3A%221892a8284422db-0bdb5abb4196568-3f626b4b-1d03d0-1892a8284436913%22%2C%22%24user_state%22%3A%22anonymous%22%2C%22%24sesid%22%3A%5B1688635345107%2C%221892a828445af-0901201d945bb4-3f626b4b-1d03d0-1892a8284467d90%22%2C1688635343941%5D%2C%22%24session_recording_enabled_server_side%22%3Atrue%2C%22%24console_log_recording_enabled_server_side%22%3Atrue%2C%22%24session_recording_recorder_version_server_side%22%3A%22v1%22%2C%22%24autocapture_disabled_server_side%22%3Afalse%2C%22%24active_feature_flags%22%3A%5B%5D%2C%22%24enabled_feature_flags%22%3A%7B%7D%2C%22%24feature_flag_payloads%22%3A%7B%7D%7D; _cc_id=d25d20359be494ce8a946969ae893796; panoramaId=2f1c9d627c3693502d37dbe0a0ae16d53938b935b485fb3d07f73ee5c66cdb42; panoramaIdType=panoIndiv; panoramaId_expiry=1689239949527; euconsent-v2=CPttmcAPttmcAAZACBENDJCsAP_AAH_AAAAAJgNX_H__bW9r8f7_aft0eY1P9_j77uQxBhfJk-4F3LvW-JwX52E7NF16tqoKmR4Eu3LBIUNlHNHUTVmwaokVryHsak2cpTNKJ6BEkHMRO2dYCF5vmxtjeQKY5_p_d3fx2D-t_dv-39z3z81Xn3dZf-_0-PCdU5_9Dfn9fRfb-9IP9_78v8v8_9_rk2_eT13_79_7_H9-f_87_BMEAkw1LiALsShwJtAwihRAjCsICKBQAAEAwNEBAA4MCnRGAT6wiQAoBQBGBECHAFGRAIAAAIAkIgAkCLBAAAAIBAACABAIhAAQMAgoALAQCAAEB0DFEKAAQJCBIiIiFMCAiBIICWyoQSgukNMIAqywAoBEbBQAIgABFYAAgLBwDBEgJWLBAlxBtEAAwAIBRKhWoJPTQAKGRssAAAAA.YAAAAAAAAAAA; pubconsent-v2=YAAAAAAAAAAA; fpestid=zcR1aUPinZxSDu5MufqqO5Iddd9a1Drx-pdJc4S6Lb4VMZqiivUxz7FZLnes_HTgsEKvGg',
    'Priority': 'u=3, i',
}


output_data = []

for corporate_id in corporate_ids:
    json_data = {
        'variables': {
            'id': corporate_id,
        },
        'query': 'query ($id: String!) {\n  corporate(id: $id) {\n    id\n    name\n    description\n    logo_url\n    hq_city\n    hq_country\n    website_url\n    linkedin_url\n    twitter_url\n    startup_partners_count\n    startup_partners {\n      master_startup_id\n      company_name\n      logo_url: logo\n      city\n      website\n      country\n      theme_gd\n      __typename\n    }\n    startup_themes\n    startup_friendly_badge\n    __typename\n  }\n}\n',
    }

    response = requests.post('https://ranking.glassdollar.com/graphql', cookies=cookies, headers=headers, json=json_data)

    if response.status_code == 200:
        response_json = response.json()

        corporate_data = response_json['data']['corporate']

        name = corporate_data['name']
        description = corporate_data['description']
        logo_url = corporate_data['logo_url']
        hq_city = corporate_data['hq_city']
        hq_country = corporate_data['hq_country']
        website_url = corporate_data['website_url']
        linkedin_url = corporate_data['linkedin_url']
        twitter_url = corporate_data['twitter_url']
        startup_partners_count = corporate_data['startup_partners_count']

        startup_partners = []
        for partner in corporate_data['startup_partners']:
            company_name = partner['company_name']
            partner_logo_url = partner['logo_url']
            partner_city = partner['city']
            partner_website = partner['website']
            partner_country = partner['country']
            partner_theme_gd = partner['theme_gd']
            startup_partners.append({
                'company_name': company_name,
                'logo_url': partner_logo_url,
                'city': partner_city,
                'website': partner_website,
                'country': partner_country,
                'theme_gd': partner_theme_gd
            })

        startup_themes = corporate_data['startup_themes']

        output_data.append({
            'id': corporate_id,
            'name': name,
            'description': description,
            'logo_url': logo_url,
            'hq_city': hq_city,
            'hq_country': hq_country,
            'website_url': website_url,
            'linkedin_url': linkedin_url,
            'twitter_url': twitter_url,
            'startup_partners_count': startup_partners_count,
            'startup_partners': startup_partners,
            'startup_themes': startup_themes
        })

    else:
        print(f"Request failed for corporate ID {corporate_id}. HTTP status code:", response.status_code)

# Define the file path
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
file_path = os.path.join(desktop_path, 'output.json')

# Write the data to a JSON file
with open(file_path, 'w') as json_file:
    json.dump(output_data, json_file, indent=4)

print("Data saved to:", file_path)

    
