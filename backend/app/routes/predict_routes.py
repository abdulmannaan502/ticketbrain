from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import schemas, models
from ..database import get_db
from ..auth import get_current_user
from ..ml.inference import predict_priority

router = APIRouter(prefix="/ml", tags=["ml"])


@router.post("/predict", response_model=schemas.TicketPrediction)
def predict_ticket(
    ticket: schemas.TicketIn,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
):
    label, score = predict_priority(ticket.subject, ticket.body)

    log = models.TicketLog(
        user_id=user.id,
        subject=ticket.subject,
        body=ticket.body,
        predicted_priority=label,
        predicted_confidence=score,
    )
    db.add(log)
    db.commit()

    return schemas.TicketPrediction(
        priority_label=label,
        priority_score=score,
    )
