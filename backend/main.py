from contextlib import asynccontextmanager
from fastapi import FastAPI , Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from backend.models import Product, UserCreate, UserLogin
from backend.database import session, engine, get_db
import backend.database_models as database_models
from backend.database_models import User
from backend.security import hash_password, verify_password, create_access_token, SECRET_KEY, ALGORITHM
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        
        return email

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


database_models.Base.metadata.create_all(bind=engine)

products = [
    Product(id=1,name="Phone", description="A budget phone", price=99.9,quantity=10),
    Product(id=2,name="Laptop", description="A gaming laptop",price=999.99,quantity=6),
    Product(id=3,name="Pen", description="A blue ink pen",price=1.99,quantity=100),
    Product(id=4,name="Table", description="A wodden table",price=199.99,quantity=20)
]

# def get_db():
#     db=session()
#     try:
#         yield db
#     finally:
#         db.close()

def init_db():
    db = session()
    count = db.query(database_models.Product).count()

    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        db.commit()

@asynccontextmanager
async def lifespan(_app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://stock-flow-pkkkh8trq-amaan-shikalgars-projects.vercel.app/"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def greet():
    return "welcome to Telusko Trac"

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    db_products = db.query(database_models.Product).all()
    return db_products

@app.get("/products/{id}")
def get_product_by_id(id:int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        return db_product
    return "product not found"

@app.post("/products")
def add_product(product: Product, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/products/{id}")
def update_product(id:int, product:Product, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "product updated"
    else:
        return "Product not found"

@app.delete("/products/{id}")
def delete_product(id:int, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    else:
        return "Product not found"

@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = User(
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created"}

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == form_data.username).first()

    if not db_user or not verify_password(form_data.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": db_user.email})

    return {"access_token": token, "token_type": "bearer"}

@app.get("/me")
def get_me(current_user: str = Depends(get_current_user)):
    return {"user": current_user}