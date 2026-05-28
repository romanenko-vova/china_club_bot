from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, BigInteger
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    telegram_id = Column(BigInteger, unique=True, index=True)
    username = Column(String, unique=True, nullable=True)
    email = Column(String, unique=True, index=True, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    sub_end_date = Column(DateTime, nullable=True, default=None)
    sub_ban_date = Column(DateTime, nullable=True, default=None) # date когда мы выкинем человек из канала. sub_end_date + 2 дня
    sub_status = Column(String, nullable=True, default=None) # active, banned, expired
    
    payments = relationship("Payment", back_populates="user")
    
    
class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Integer)
    status = Column(String, default="pending")
    invoice_id = Column(String, unique=True, index=True, nullable=True)
    subscription_id = Column(String, index=True, nullable=True)
    description = Column(String)
    sub_type = Column(String, index=True) # 1_month_rf, 3_month_rf, 6_month_rf, 12_month_rf, 1_month_fr, 3_month_fr, 6_month_fr, 12_month_fr
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    user = relationship("User", back_populates="payments")
