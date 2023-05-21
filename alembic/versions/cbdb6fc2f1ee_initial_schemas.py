"""initial schemas

Revision ID: cbdb6fc2f1ee
Revises: 
Create Date: 2023-03-10 23:57:58.988119

"""
from alembic import op
import sqlalchemy as sa
from pathlib import Path
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'cbdb6fc2f1ee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('brand',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('short_description', sa.Text(), nullable=True),
    sa.Column('slogan', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('slogan')
    )
    op.create_table('carrier',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('city',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('country',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('end_user_permission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('display_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('display_name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('display_name', sa.String(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description'),
    sa.UniqueConstraint('display_name')
    )
    op.create_table('inactive_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('display_name', sa.String(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description'),
    sa.UniqueConstraint('display_name')
    )
    op.create_table('item_colory',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('display_name', sa.String(), nullable=False),
    sa.Column('hex_color', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('item_size_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('item_size_geography',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('geography', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('item_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('display_name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lifecycle_state',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('display_name', sa.String(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('display_name')
    )
    op.create_table('market_source',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('display_name', sa.String(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('display_name'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('url')
    )
    op.create_table('refresh_token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('setting',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.Text(), nullable=True),
    sa.Column('expires_on', sa.DateTime(), nullable=True),
    sa.Column('revoked', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('expires_on'),
    sa.UniqueConstraint('token')
    )
    op.create_table('shipping_mode',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('address_type_id', sa.Integer(), nullable=True),
    sa.Column('org_name', sa.String(), nullable=False),
    sa.Column('address1', sa.String(), nullable=False),
    sa.Column('address2', sa.String(), nullable=True),
    sa.Column('country_id', sa.Integer(), nullable=True),
    sa.Column('city_id', sa.Integer(), nullable=True),
    sa.Column('zipcode', sa.String(length=40), nullable=False),
    sa.ForeignKeyConstraint(['address_type_id'], ['address_type.id'], ),
    sa.ForeignKeyConstraint(['city_id'], ['city.id'], ),
    sa.ForeignKeyConstraint(['country_id'], ['country.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('org_name')
    )
    op.create_table('attribute',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('display_name', sa.String(), nullable=False),
    sa.Column('data_type', sa.String(), nullable=False),
    sa.Column('minimum_length', sa.Integer(), nullable=True),
    sa.Column('maximum_length', sa.Integer(), nullable=True),
    sa.Column('searchable', sa.Boolean(), nullable=True),
    sa.Column('end_user_permission_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['end_user_permission_id'], ['end_user_permission.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('display_name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('country_cities',
    sa.Column('country_id', sa.Integer(), nullable=True),
    sa.Column('city_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['city_id'], ['city.id'], ),
    sa.ForeignKeyConstraint(['country_id'], ['country.id'], )
    )
    op.create_table('item_size',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('size_category_id', sa.Integer(), nullable=True),
    sa.Column('sort_key', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['size_category_id'], ['item_size_category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('email_verified', sa.Boolean(), nullable=True),
    sa.Column('free_form_policies', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('last_successful_login', sa.DateTime(), nullable=True),
    sa.Column('previous_successful_login', sa.DateTime(), nullable=True),
    sa.Column('user_status_id', sa.Integer(), nullable=True),
    sa.Column('mfa_activated', sa.Boolean(), nullable=True),
    sa.Column('inactive_status_id', sa.Integer(), nullable=True),
    sa.Column('lifecycle_state_id', sa.Integer(), nullable=True),
    sa.Column('is_npe', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['inactive_status_id'], ['inactive_status.id'], ),
    sa.ForeignKeyConstraint(['lifecycle_state_id'], ['lifecycle_state.id'], ),
    sa.ForeignKeyConstraint(['user_status_id'], ['user_status.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('password'),
    sa.UniqueConstraint('username'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('item_regional_size',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_size_id', sa.Integer(), nullable=False),
    sa.Column('size_geography_id', sa.Integer(), nullable=False),
    sa.Column('effective_size', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['item_size_id'], ['item_size.id'], ),
    sa.ForeignKeyConstraint(['size_geography_id'], ['item_size_geography.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shipping_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('shipping_mode_id', sa.Integer(), nullable=True),
    sa.Column('carrier_id', sa.Integer(), nullable=True),
    sa.Column('address_id', sa.Integer(), nullable=False),
    sa.Column('instructions', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['address_id'], ['address.id'], ),
    sa.ForeignKeyConstraint(['carrier_id'], ['carrier.id'], ),
    sa.ForeignKeyConstraint(['shipping_mode_id'], ['shipping_mode.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_addresses',
    sa.Column('address_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['address_id'], ['address.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('user_attributes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('attribute_id', sa.Integer(), nullable=False),
    sa.Column('attribute_value', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['attribute_id'], ['attribute.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'attribute_id')
    )
    op.create_table('user_groups',
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['group.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('item_size', sa.Float(), nullable=False),
    sa.Column('regional_size_id', sa.Integer(), nullable=True),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.Column('listing_price', sa.Numeric(), nullable=False),
    sa.Column('acquisition_price', sa.Numeric(), nullable=True),
    sa.Column('market_price', sa.Numeric(), nullable=False),
    sa.Column('unrealised_profit', sa.Numeric(), nullable=True),
    sa.Column('size', sa.Integer(), nullable=False),
    sa.Column('currency', sa.String(), nullable=False),
    sa.Column('colory_id', sa.Integer(), nullable=True),
    sa.Column('brand_id', sa.Integer(), nullable=True),
    sa.Column('market_source_id', sa.Integer(), nullable=True),
    sa.Column('listed_by_id', sa.Integer(), nullable=True),
    sa.Column('seller_id', sa.Integer(), nullable=True),
    sa.Column('buyer_id', sa.Integer(), nullable=True),
    sa.Column('shipping_info_id', sa.Integer(), nullable=True),
    sa.Column('is_public', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['brand_id'], ['brand.id'], ),
    sa.ForeignKeyConstraint(['buyer_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['colory_id'], ['item_colory.id'], ),
    sa.ForeignKeyConstraint(['listed_by_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['market_source_id'], ['brand.id'], ),
    sa.ForeignKeyConstraint(['regional_size_id'], ['item_regional_size.id'], ),
    sa.ForeignKeyConstraint(['seller_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['shipping_info_id'], ['shipping_info.id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['item_status.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('user_items',
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    # ### end Alembic commands ###

    with open(str(Path(__file__).with_suffix('')) + '_up.sql', 'r', encoding='utf-8') as f:
        op.execute(f.read())


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_items')
    op.drop_table('item')
    op.drop_table('user_groups')
    op.drop_table('user_attributes')
    op.drop_table('user_addresses')
    op.drop_table('shipping_info')
    op.drop_table('item_regional_size')
    op.drop_table('user')
    op.drop_table('item_size')
    op.drop_table('country_cities')
    op.drop_table('attribute')
    op.drop_table('address')
    op.drop_table('user_status')
    op.drop_table('shipping_mode')
    op.drop_table('setting')
    op.drop_table('refresh_token')
    op.drop_table('market_source')
    op.drop_table('lifecycle_state')
    op.drop_table('item_status')
    op.drop_table('item_size_geography')
    op.drop_table('item_size_category')
    op.drop_table('item_colory')
    op.drop_table('inactive_status')
    op.drop_table('group')
    op.drop_table('end_user_permission')
    op.drop_table('country')
    op.drop_table('city')
    op.drop_table('carrier')
    op.drop_table('brand')
    op.drop_table('address_type')
    # ### end Alembic commands ###

    with open(str(Path(__file__).with_suffix('')) + '_down.sql', 'r', encoding='utf-8') as f:
        op.execute(f.read())