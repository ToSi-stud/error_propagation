import math
import sympy as sp

def fehlerfortpflanzung(datasets):
    avgs = []
    standartabweichungen = []
    deltax = []
    quad_avgs = []
    product_avg = sum([x * y for x, y in zip(datasets[0], datasets[1])]) / len(datasets[0])
    for dataset in datasets:
        avgs.append(sum(dataset) / len(dataset))
        quad_avgs.append(sum([x ** 2 for x in dataset]) / len(dataset))

    for i in range(len(datasets)):
        standartabweichungen.append(math.sqrt(sum([(x - avgs[i]) ** 2 for x in datasets[i]]) / (len(datasets[i]) - 1)))

    for i in range(len(datasets)):
        deltax.append(standartabweichungen[i] / math.sqrt(len(datasets[i])))

    y_Achsenabschnitt_den = quad_avgs[0] - avgs[0] ** 2
    y_Achsenabschnitt_nom = quad_avgs[0] * avgs[1] - avgs[0] * product_avg
    y_Achsenabschnitt = y_Achsenabschnitt_nom / y_Achsenabschnitt_den

    steigung_den = quad_avgs[0] - avgs[0] ** 2
    steigung_nom = product_avg - avgs[0] * avgs[1]
    steigung = steigung_nom / steigung_den

    delta_y_Achsenabschnitt_den = quad_avgs[0] - avgs[0] ** 2
    delta_y_Achsenabschnitt_nom = quad_avgs[0] * (quad_avgs[1] - steigung * product_avg - y_Achsenabschnitt * avgs[1])
    delta_y_Achsenabschnitt_quad = delta_y_Achsenabschnitt_nom / delta_y_Achsenabschnitt_den / (len(datasets[0]) - 2)
    delta_y_Achsenabschnitt = math.sqrt(delta_y_Achsenabschnitt_quad)

    delta_steigung_den = quad_avgs[0] - avgs[0] ** 2
    delta_steigung_nom = quad_avgs[1] - steigung * product_avg - y_Achsenabschnitt * avgs[1]
    delta_steigung_quad = delta_steigung_nom / delta_steigung_den / (len(datasets[0]) - 2)
    delta_steigung = math.sqrt(delta_steigung_quad)

    quad_Korrelationskoeffizient_nom = (product_avg - avgs[0] * avgs[1]) ** 2
    quad_Korrelationskoeffizient_den = (quad_avgs[0] - avgs[0] ** 2) * (quad_avgs[1] - avgs[1] ** 2)
    quad_Korrelationskoeffizient = quad_Korrelationskoeffizient_nom / quad_Korrelationskoeffizient_den
    
    # optional output may remove wenn lust wa
    richtmoment = 4 * math.pi**2 / steigung
    delta_richtmoment = math.sqrt((4 * math.pi**2 / steigung**2 * delta_steigung) ** 2)
    j_tisch = y_Achsenabschnitt * richtmoment/ (4 * math.pi**2)
    
    delta_j_tisch_1 = (richtmoment / (4 * math.pi**2) * delta_y_Achsenabschnitt)**2
    delta_j_tisch_2 = (y_Achsenabschnitt * delta_richtmoment / (4 * math.pi**2))**2
    delta_j_tisch = math.sqrt(delta_j_tisch_1 + delta_j_tisch_2)

    js_inhomogen_1 = y_Achsenabschnitt * richtmoment/ (4 * math.pi**2) - j_tisch

    delta_js_inhomogen_1 = richtmoment / (4 * math.pi**2) * delta_y_Achsenabschnitt
    delta_js_inhomogen_2 = y_Achsenabschnitt * delta_richtmoment / (4 * math.pi**2)
    delta_js_inhomogen = math.sqrt(delta_js_inhomogen_1 ** 2 + delta_js_inhomogen_2 ** 2 + delta_j_tisch ** 2)



    u,i = sp.symbols('u i')
    wiederstand_fromel = u / i
    partielle_ableitung_wiederstand_u = sp.diff(wiederstand_fromel, u)
    partielle_ableitung_wiederstand_i = sp.diff(wiederstand_fromel, i)

    Gesamtfehler_systematisch = sum([abs(partielle_ableitung_wiederstand_u.subs({u : avgs[0], i : avgs[1]})) * deltax[0], abs(partielle_ableitung_wiederstand_i.subs({u : avgs[0], i : avgs[1]})) * deltax[1]])
    Gesamtfehler_zufällig = math.sqrt(sum([(partielle_ableitung_wiederstand_u.subs({u : avgs[0], i : avgs[1]}) * deltax[0]) ** 2, (partielle_ableitung_wiederstand_i.subs({u : avgs[0], i : avgs[1]}) * deltax[1]) ** 2]))
    R = 1/steigung * 1000
    return {'Gesamtfehler_systematisch': Gesamtfehler_systematisch, 
            'Gesamtfehler_zufällig': Gesamtfehler_zufällig, 
            'R': R, 
            'y_Achsenabschnitt': y_Achsenabschnitt,
            'steigung': steigung,
            'delta_y_Achsenabschnitt': delta_y_Achsenabschnitt,
            'delta_steigung': delta_steigung,
            'quad_Korrelationskoeffizient': quad_Korrelationskoeffizient,
            'deltax': deltax,
            'standartabweichungen': standartabweichungen,
            'avgs': avgs,
            'richtmoment': richtmoment,
            'delta_richtmoment': delta_richtmoment,
            'j_tisch': j_tisch,
            'delta_j_tisch': delta_j_tisch,
            'js_inhomogen': js_inhomogen_1,
            'delta_js_inhomogen': delta_js_inhomogen
            }