"""Description of the changes

Revision ID: 0eacc72c6c31
Revises: 60be538e8174
Create Date: 2023-10-17 13:19:09.597084

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0eacc72c6c31'
down_revision: Union[str, None] = '60be538e8174'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'wallet', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'wallet', type_='unique')
    # ### end Alembic commands ###
