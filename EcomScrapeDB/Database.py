from sqlalchemy import create_engine, Column, Integer, update, delete, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Importing data scraped from different e-commerce websites
""" Star Tech Imports """
from StarTech import link_list, all_prices, product_model_list

""" Tech Land Imports """
from TechLand import tech_link_list, tech_laptop_name_list, tech_laptop_prices

""" Ryans Imports """
from RYans import ryans_product_price, ryans_product_models, ryans_product_url

# Create a SQLite database engine for managing product data
engine = create_engine("sqlite:///products.db", echo=True)

# Declare the base class for SQLAlchemy ORM
Base = declarative_base()

# Configure a session factory for managing database transactions
Session = sessionmaker(bind=engine)
session = Session()

# Define the table schema for Star Tech products
class StarTechProducts(Base):
    __tablename__ = "Starproducts"  # Table name in the database

    id = Column(Integer, primary_key=True)  # Primary key column
    star_model = Column(String)  # Product model name column
    star_price = Column(Integer)  # Product price column
    star_url = Column(String)  # Product URL column

# Define the table schema for Tech Land products
class TechLandProducts(Base):
    __tablename__ = "Techproducts"  # Table name in the database

    id = Column(Integer, primary_key=True)  # Primary key column
    tech_model = Column(String)  # Product model name column
    tech_price = Column(Integer)  # Product price column
    tech_url = Column(String)  # Product URL column

# Define the table schema for Ryans products
class RyanProducts(Base):
    __tablename__ = "Ryanproducts"  # Table name in the database

    id = Column(Integer, primary_key=True)  # Primary key column
    ryan_model = Column(String)  # Product model name column
    ryan_price = Column(Integer)  # Product price column
    ryan_url = Column(String)  # Product URL column

if __name__ == "__main__":

    # Create the database tables based on the defined schemas
    Base.metadata.create_all(engine)

    """ For Star Tech """
    # Iterate over the Star Tech data and insert it into the Starproducts table
    for model, price, url in zip(product_model_list, all_prices, link_list):
        product = StarTechProducts(star_model=model, star_price=price, star_url=url)
        session.add(product)  # Add each product record to the session

    """ For Tech Land """
    # Iterate over the Tech Land data and insert it into the Techproducts table
    for model, price, url in zip(tech_laptop_name_list, tech_laptop_prices, tech_link_list):
        tech_product = TechLandProducts(tech_model=model, tech_price=price, tech_url=url)
        session.add(tech_product)  # Add each product record to the session

    """ For Ryans """
    # Iterate over the Ryans data and insert it into the Ryanproducts table
    for model, price, url in zip(ryans_product_models, ryans_product_price, ryans_product_url):
        ryan_products = RyanProducts(ryan_model=model, ryan_price=price, ryan_url=url)
        session.add(ryan_products)  # Add each product record to the session

    # Commit all changes to the database
    session.commit()

    # Close the database session
    session.close()
