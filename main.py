from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/dataset-pokemon")
def get_pokemon_data():
    dataset = []
    # Vamos pegar os primeiros 80 para ter um dataset curto e rápido
    for i in range(1, 1000):
        url = f"https://pokeapi.co/api/v2/pokemon/{i}"
        res = requests.get(url).json()
        
        # Extraindo colunas variadas
        info = {
            "nome": res["name"],
            "altura": res["height"],
            "peso": res["weight"],
            "experiencia_base": res["base_experience"],
            "tipo_principal": res["types"][0]["type"]["name"],
            "hp": res["stats"][0]["base_stat"],
            "ataque": res["stats"][1]["base_stat"],
            "defesa": res["stats"][2]["base_stat"],
            "ataque_especial": res["stats"][3]["base_stat"],
            "defesa_especial": res["stats"][4]["base_stat"],
            "velocidade": res["stats"][5]["base_stat"],
            "qtd_habilidades": len(res["abilities"]),
            "qtd_movimentos": len(res["moves"]), 
            
        }
        dataset.append(info)
    
    return dataset