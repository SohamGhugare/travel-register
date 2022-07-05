import yaml

def read_routes():
    with open("routes.yaml") as f:
        routes = yaml.load(f, Loader=yaml.FullLoader)
    return routes["routes"]

def fetch_users():
    with open("users.yaml") as f:
        users = yaml.load(f, Loader=yaml.FullLoader)
    return users or {}

def add_user(name, mode, route, stop):
    users = fetch_users()
    users[name] = {
            "mode": mode,
            "route": route,
            "stop": stop
        }
    
    with open("users.yaml", "w") as f:
        yaml.dump(users, f)

    return True

if __name__ == '__main__':
    print(add_user(name="Shivaji", mode="bus", route="route-2", stop="stop 3"))