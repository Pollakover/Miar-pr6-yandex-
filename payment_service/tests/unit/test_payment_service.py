import pytest
from uuid import uuid4
from app.models.payment import Payment
from app.schemas.payment_schema import PaymentDB
from app.services.payment_service import PaymentService


@pytest.fixture
def sample_payment():
    return {
        "id": uuid4(),
        "amount": 100.50,
        "currency": "USD",
        "status": "created"
    }

def test_payment_model_creation(sample_payment):
    """Проверка корректности создания объекта Payment"""
    payment = Payment(**sample_payment)
    assert payment.amount == 100.50
    assert payment.currency == "USD"
    assert payment.status == "created"

def test_payment_schema_validation(sample_payment):
    """Проверка валидации схемы PaymentSchema"""
    schema = PaymentDB(**sample_payment)
    assert schema.currency == "USD"
    assert isinstance(schema.id, type(uuid4()))