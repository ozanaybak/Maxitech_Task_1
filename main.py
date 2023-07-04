from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import requests
import os
import json

app = FastAPI()

@app.get("/glassdollar")
async def crawl_glassdollar():
    try:
        cookies = {
            '_ga': 'GA1.1.76544189.1687342534',
            '_ga_SX8XLCG27H': 'GS1.1.1687440958.3.1.1687440959.0.0.0',
            '_gid': 'GA1.2.575591500.1687342534',
            'euconsent-v2': 'CPttmcAPttmcAAZACBENDJCsAP_AAH_AAAAAJgNX_H__bW9r8f7_aft0eY1P9_j77uQxBhfJk-4F3LvW-JwX52E7NF16tqoKmR4Eu3LBIUNlHNHUTVmwaokVryHsak2cpTNKJ6BEkHMRO2dYCF5vmxtjeQKY5_p_d3fx2D-t_dv-39z3z81Xn3dZf-_0-PCdU5_9Dfn9fRfb-9IP9_78v8v8_9_rk2_eT13_79_7_H9-f_87_BMEAkw1LiALsShwJtAwihRAjCsICKBQAAEAwNEBAA4MCnRGAT6wiQAoBQBGBECHAFGRAIAAAIAkIgAkCLBAAAAIBAACABAIhAAQMAgoALAQCAAEB0DFEKAAQJCBIiIiFMCAiBIICWyoQSgukNMIAqywAoBEbBQAIgABFYAAgLBwDBEgJWLBAlxBtEAAwAIBRKhWoJPTQAKGRssAAAAA.YAAAAAAAAAAA',
            'pubconsent-v2': 'YAAAAAAAAAAA',
            '_cc_id': 'd25d20359be494ce8a946969ae893796',
            'panoramaId': 'ecd5f0ec049f28d91e661868159e4945a7025dc77205a293f6383dcdeb90f06d',
            'panoramaIdType': 'panoIndiv',
            'panoramaId_expiry': '1687947334845',
            'fpestid': 'zcR1aUPinZxSDu5MufqqO5Iddd9a1Drx-pdJc4S6Lb4VMZqiivUxz7FZLnes_HTgsEKvGg',
        }

        headers = {
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'Origin': 'https://ranking.glassdollar.com',
            'Referer': 'https://ranking.glassdollar.com/corporates/8483fc50-b82d-5ffa-5f92-6c72ac4bdaff',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
        }

        json_data = {
            'variables': {
                'id': '8483fc50-b82d-5ffa-5f92-6c72ac4bdaff',
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

            output_data = {
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
            }

            return JSONResponse(content=output_data)
        else:
            raise HTTPException(status_code=response.status_code, detail="Request failed")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
