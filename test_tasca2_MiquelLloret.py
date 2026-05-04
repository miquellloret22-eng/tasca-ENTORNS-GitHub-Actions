import tasca_escrita1
import tasca_escrita2
import unittest

class Test1(unittest.TestCase):
    def test_buscar_per_titol_existent(self):
        """
        comprova que la funció buscar_per_titol retorna el videojoc correctequan el títol existeix
        """
        joc = tasca_escrita1.buscar_per_titol("cyberpunk 2077", tasca_escrita1.videojocs)
        if joc is not None and joc["titol"] == "Cyberpunk 2077":
            print("test_buscar_per_titol_existent: OK")
        else:
            print("test_buscar_per_titol_existent: ERROR")
    
    def test_buscar_per_titol_inexistent(self):
        """
        comprova que la funció buscar_per_titol retorna None quan el videojoc no existeix
        """
        joc = tasca_escrita1.buscar_per_titol("Mario Kart", tasca_escrita1.videojocs)
        if joc is None:
            print("test_buscar_per_titol_inexistent: OK")
        else:
            print("test_buscar_per_titol_inexistent: ERROR")
    
    def test_afegir_a_biblioteca_correcte(self):
        """
        comprova que afegir_a_biblioteca afegeix correctament un joc a la biblioteca quan existeix i no està repetit
        """
        biblioteca = []
        resultat = tasca_escrita1.afegir_a_biblioteca("FIFA 24", tasca_escrita1.videojocs, biblioteca)
        if resultat == "✅ Joc afegit!" and len(biblioteca) == 1:
            print("test_afegir_a_biblioteca_correcte: OK")
        else:
            print("test_afegir_a_biblioteca_correcte: ERROR")
    
    def test_afegir_a_biblioteca_repetit(self):
        """
        comprova que afegir_a_biblioteca detecta un joc repetit dins la biblioteca personal
        """
        biblioteca = []
        tasca_escrita1.afegir_a_biblioteca("FIFA 24", tasca_escrita1.videojocs, biblioteca)
        resultat = tasca_escrita1.afegir_a_biblioteca("FIFA 24", tasca_escrita1.videojocs, biblioteca)
        if resultat == "⚠️ Ja està a la biblioteca":
            print("test_afegir_a_biblioteca_repetit: OK")
        else:
            print("test_afegir_a_biblioteca_repetit: ERROR")
    
    def test_joc_mes_car(self):
        """
        comprova que la funció joc_mes_car retorna el videojoc amb el preu més alt del catàleg
        """
        joc = tasca_escrita1.joc_mes_car(tasca_escrita1.videojocs)
        if joc["titol"] == "FIFA 24":
            print("test_joc_mes_car: OK")
        else:
            print("test_joc_mes_car: ERROR")

class Test2(unittest.TestCase):
    def test_crear_sequencia_valid(self):
        """
        comprova que la funció crear_sequencia genera correctament una llista de números entre dos enters vàlids
        """
        resultat = tasca_escrita2.crear_sequencia(5, 10)
        if resultat == [5, 6, 7, 8, 9, 10]:
            print("test_crear_sequencia_valid: OK")
        else:
            print("test_crear_sequencia_valid: ERROR")

    def test_crear_sequencia_invalid(self):
        """
        comprova que la funció crear_sequencia retorna una llista buida quan els paràmetres no són vàlids
        """
        resultat = tasca_escrita2.crear_sequencia(10, 5)
        if resultat == []:
            print("test_crear_sequencia_invalid: OK")
        else:
            print("test_crear_sequencia_invalid: ERROR")

    def test_numeros_imparells_majors(self):
        """
        comprova que la funció numeros_imparells_majors retorna només els números senars majors que el límit indicat
        """
        llista = [3, -1, 7, 2, -1, 9, 4, 7]
        resultat = tasca_escrita2.numeros_imparells_majors(llista, 3)
        if resultat == [7, 9, 7]:
            print("test_numeros_imparells_majors: OK")
        else:
            print("test_numeros_imparells_majors: ERROR")

    def test_primera_posicio(self):
        """
        comprova que la funció primera_posicio retorna la posició correcta de la primera aparició d’un element o -1 si no existeix
        """
        llista = [3, -1, 7, 2, -1, 9, 4, 7]
        resultat = tasca_escrita2.primera_posicio(llista, 7)
        if resultat == 2:
            print("test_primera_posicio: OK")
        else:
            print("test_primera_posicio: ERROR")

    def test_diagonal_principal(self):
        """
        comprova que la funció diagonal_principal retorna correctament la diagonal principal d’una matriu quadrada
        """
        matriu = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        resultat = tasca_escrita2.diagonal_principal(matriu)
        if resultat == [1, 5, 9]:
            print("test_diagonal_principal: OK")
        else:
            print("test_diagonal_principal: ERROR")

if __name__ == "__main__":
    unittest.main()
    