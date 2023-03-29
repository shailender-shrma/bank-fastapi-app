from fastapi import FastAPI
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/bank-list/RTGS-HO", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json() == {"ifsc":"ABHY0065001","branch":"RTGS-HO","address":"ABHYUDAYA BANK BLDG., B.NO.71, NEHRU NAGAR, KURLA (E), MUMBAI-400024","city":"MUMBAI","district":"GREATER MUMBAI","state":"MAHARASHTRA","banks":[{"name":"ABHYUDAYA COOPERATIVE BANK LIMITED"},{"name":"THE ROYAL BANK OF SCOTLAND N V"},{"name":"ABU DHABI COMMERCIAL BANK"},{"name":"THE AKOLA DISTRICT CENTRAL COOPERATIVE BANK"},{"name":"AKOLA JANATA COMMERCIAL COOPERATIVE BANK"},{"name":"AHMEDABAD MERCANTILE COOPERATIVE BANK"},{"name":"ANDHRA BANK"},{"name":"AUSTRALIA AND NEW ZEALAND BANKING GROUP LIMITED"},{"name":"THE ANDHRA PRADESH STATE COOPERATIVE BANK LIMITED"},{"name":"ANDHRA PRAGATHI GRAMEENA BANK"},{"name":"APNA SAHAKARI BANK LIMITED"},{"name":"ALMORA URBAN COOPERATIVE BANK LIMITED"},{"name":"BASSEIN CATHOLIC COOPERATIVE BANK LIMITED"},{"name":"BANK OF BARODA"},{"name":"BARCLAYS BANK"},{"name":"BANK OF BAHARAIN AND KUWAIT BSC"},{"name":"BHARAT COOPERATIVE BANK MUMBAI LIMITED"},{"name":"BANK OF CEYLON"},{"name":"DENA BANK"},{"name":"BANK OF INDIA"},{"name":"BHARATIYA MAHILA BANK LIMITED"},{"name":"BANK OF AMERICA"},{"name":"CITIZEN CREDIT COOPERATIVE BANK LIMITED"},{"name":"JP MORGAN BANK"},{"name":"CITI BANK"},{"name":"CITY UNION BANK LIMITED"},{"name":"CAPITAL LOCAL AREA BANK LIMITED"},{"name":"CORPORATION BANK"},{"name":"CREDIT SUISEE AG"},{"name":"SHRI CHHATRAPATI RAJASHRI SHAHU URBAN COOPERATIVE"},{"name":"CATHOLIC SYRIAN BANK LIMITED"}]}

def test_not_read_main():
    response = client.get("/bank-list/oops", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 400
    assert response.json() == {"detail":"Branch name doesn't exist."}