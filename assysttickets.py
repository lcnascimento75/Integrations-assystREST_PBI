import requests
import json

# --- AVISO DE SEGURANÇA ---
# As credenciais abaixo foram fornecidas por você.
# NUNCA coloque senhas diretamente no código em um ambiente de produção.
ASSYST_USERNAME = ''
ASSYST_PASSWORD = ''

# --- CONFIGURAÇÃO DO PROXY ---
# Adicione o dicionário de proxies conforme sua necessidade.
proxies = {
   'http': '',
   'https': '',
}

# URL do endpoint de tickets.
URL = "http://sistemas.tjes.jus.br:8080/assystREST/v2/assysttickets"

print(f"Tentando acessar a URL: {URL}")
print(f"Usando o proxy: {proxies['http']}")

try:
    # Adicionamos o parâmetro 'proxies' à chamada da função.
    # A requisição será feita através do endereço 10.100.198.101:9090.
    response = requests.get(
        URL,
        auth=(ASSYST_USERNAME, ASSYST_PASSWORD),
        proxies=proxies
    )

    # Verifica se a requisição foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        print("\n✅ Conexão bem-sucedida!")
        try:
            tickets_data = response.json()
            print(json.dumps(tickets_data, indent=2, ensure_ascii=False))
        except json.JSONDecodeError:
            print("Não foi possível decodificar a resposta como JSON. Exibindo como texto:")
            print(response.text)

    # Trata erros comuns de autenticação e de recurso não encontrado
    elif response.status_code == 401:
        print("\n❌ Erro 401: Falha na autenticação. Verifique o usuário e a senha.")
    elif response.status_code == 403:
         print("\n❌ Erro 403: Proibido. Suas credenciais são válidas, mas não têm permissão para acessar este recurso.")
    elif response.status_code == 404:
        print("\n❌ Erro 404: Não encontrado. O endpoint '/assysttickets' não existe ou o caminho está incorreto.")
    else:
        # Para outros erros HTTP
        print(f"\n❌ Erro inesperado: {response.status_code}")
        print(f"Resposta do servidor: {response.text}")

except requests.exceptions.ProxyError as e:
    # Erro específico para falha de conexão com o proxy
    print(f"\n❌ Erro de Proxy: Não foi possível conectar ao proxy em {proxies['http']}.")
    print(f"Detalhes: {e}")
except requests.exceptions.RequestException as e:
    # Para outros erros de conexão (ex: DNS, rede, etc.)
    print(f"\n❌ Erro de conexão: {e}")
