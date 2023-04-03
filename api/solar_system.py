import requests, json

class PlanetaryAPI(object):
    '''Python Object used for retrieving information about our solar system from an Open API'''

    actual_solar_system    = "https://api.le-systeme-solaire.net/rest/bodies"
    custom_solar_system    = "http://localhost:8080/planets/"


    @staticmethod
    def populate(planet) -> int:
        '''Populates the custom solar system with a planet.'''
        response = requests.post(PlanetaryAPI.custom_solar_system, data=planet)
        return response.status_code

    @staticmethod
    def get_planets() -> None:
        '''Gets all planets from the Open API and populates them using the populate method.'''
        response = requests.get(PlanetaryAPI.actual_solar_system)

        response = response.json()
        
        bodies = response['bodies']

        for body in bodies:
            if body['vol']:
                volume_value    = body['vol'].get('volValue', None)
                volume_exponent = body['vol'].get('volExponent', None)
            else:
                volume_value    = ""
                volume_exponent = ""

            if body['mass']:
                mass_value      = body['mass'].get('massValue', None)
                mass_exponent   = body['mass'].get('massExponent', None)
            else:
                mass_value      = ""
                mass_exponent   = ""

            if body['aroundPlanet']:
                orbiting        = body['aroundPlanet'].get('planet', None)
            else:
                orbiting        = None

            json_data = {
                'name'              : body.get('id'),
                'mass_value'        : mass_value,
                'mass_exponent'     : mass_exponent,
                'volume_value'      : volume_value,
                'volume_exponent'   : volume_exponent, 
                'gravity_constant'  : body.get('gravity'),
                'orbiting'          : orbiting
            }
            response = PlanetaryAPI.populate(json_data)


if __name__ == "__main__":
	PlanetaryAPI.get_planets()