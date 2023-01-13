"""creacion tabla categorias_productos

Revision ID: e05adf61c01a
Revises: ce564ad0cf2b
Create Date: 2023-01-12 19:52:43.506438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e05adf61c01a'
down_revision = 'ce564ad0cf2b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categorias_productos',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('categoria_id', sa.Integer(), nullable=False),
    sa.Column('producto_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['categoria_id'], ['categorias.id'], ),
    sa.ForeignKeyConstraint(['producto_id'], ['productos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('categorias_productos')
    # ### end Alembic commands ###
