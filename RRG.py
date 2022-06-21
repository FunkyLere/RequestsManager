# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 21:20:50 2022

@author: LENOVO
"""

import pruebas
import random
import Profile


def getRandomRegisters(master, number_of_registers):
    names = [Profile.Profile.profiles['piwok1'], Profile.Profile.profiles['piwok2'], Profile.Profile.profiles['piwok3'], Profile.Profile.profiles['piwok4'], Profile.Profile.profiles['piwok5']]
    station_names = ['Oviedo', 'Gijon', 'Leon', 'Salamanca', 'Zamora']
    station_IDs = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
    budgets = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    descriptions = ['1Description1', '2Description2', '3Description3', '4Description4', '5Description5', '6Description6', '7Description7', '8Description8', '9Description9']
    contracts = [True, False]
    contractors = ['1Contractor1', '2Contractor2', '3Contractor3', '4Contractor4', '5Contractor5', '6Contractor6', '7Contractor7', '8Contractor8', '9Contractor9']
    # formal_names = ['Julio', 'Ignacio', 'David', 'Elena', 'Susana', 'Maria', 'Reinaldo']
    # apellidos = ['1apellido1', '2apellido2', '3apellido3', '4apellido4', '5apellido5', '6apellido6', '7apellido7','8apellido8', '9apellido9']
    # cargos = ['1cargo1', '3cargo3', '4cargo4', '5cargo5', '6cargo6', '7cargo7', '8cargo8', '2cargo2', '9cargo9']
    # fotos = ['foto_1', 'foto_2', 'foto_3', 'foto_4', 'foto_5']
    dates = ['1Date1', '2Date2', '3Date3', '4Date4', '5Date5', '6Date6', '7Date7', '8Date8', '9Date9']
            
    registros = []
    for i in range(number_of_registers):
        # name = random.choice (names)
        station_name = random.choice(station_names)
        station_ID = random.choice(station_IDs)
        budget = random.choice(budgets)
        description = random.choice(descriptions)
        contract = random.choice(contracts)
        contractor = random.choice(contractors)
        creator_profile =random.choice(names)
        creation_date = random.choice(dates)
        petition_profile = random.choice(names)
        petition_date = random.choice(dates)
        visado_profile = random.choice(names)
        visado_date = random.choice(dates)
        devengo_profile = random.choice(names)
        devengo_date = random.choice(dates)
        autorization_profile = random.choice(names)
        autorization_date = random.choice(dates)
        
        registros.append(pruebas.Register(master, station_ID, station_name, description, budget, contract, contractor,
            creator_profile.user_name, creation_date, petition_profile.user_name, petition_date, visado_profile.user_name, visado_date, devengo_profile.user_name, devengo_date, autorization_profile.user_name, autorization_date))

    return registros



