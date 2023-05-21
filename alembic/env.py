from logging.config import fileConfig

from alembic import context
from sqlalchemy import MetaData, engine_from_config
from sqlalchemy import pool

from falcon_api_boilerplate.models import GroupModel, UserModel, UserStatusModel, ItemModel, EndUserPermissionModel, ItemSizeModel, \
    ItemSizeGeographyModel, ItemRegionalSizeModel, ItemSizeCategoryModel, AttributeModel, InactiveStatusModel, \
    LifecycleStateModel, RefreshTokenModel, ItemStatusModel, ItemColoryModel, CarrierModel, ShippingModeModel, \
    ShippingInfoModel, AddressModel, AddressTypeModel, CountryModel, CityModel, RefreshToken, \
    UserAttributeAssociationModel, BrandModel, MarketSourceModel, PasswordResetTokenModel, CurrencyModel
from falcon_api_boilerplate.utils.config import get_config

config = context.config

config.set_main_option('sqlalchemy.url', get_config('db.main.database-uri'))

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)


def combine_metadata(*args):
    m = MetaData()
    for metadata in args:
        for t in metadata.tables.values():
            t.tometadata(m)
    return m


target_metadata = combine_metadata(
    GroupModel.metadata, UserModel.metadata, ItemModel.metadata, EndUserPermissionModel.metadata,
    ItemSizeModel.metadata, ItemSizeGeographyModel.metadata, ItemRegionalSizeModel.metadata,
    ItemSizeCategoryModel.metadata, AttributeModel.metadata, InactiveStatusModel.metadata, LifecycleStateModel.metadata,
    RefreshTokenModel.metadata, ItemStatusModel.metadata, ItemColoryModel.metadata, CarrierModel.metadata,
    ShippingModeModel.metadata, ShippingInfoModel.metadata, AddressModel.metadata, AddressTypeModel.metadata,
    CountryModel.metadata, CityModel.metadata, UserStatusModel.metadata, RefreshToken.metadata,
    UserAttributeAssociationModel.metadata, BrandModel.metadata, MarketSourceModel.metadata,
    PasswordResetTokenModel.metadata, CurrencyModel.metadata
)


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata,
            version_table_schema=target_metadata.schema,
            include_schemas=True
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
