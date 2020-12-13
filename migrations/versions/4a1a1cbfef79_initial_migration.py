"""Initial Migration

Revision ID: 4a1a1cbfef79
Revises: 3abaedd445a5
Create Date: 2020-12-13 11:49:15.409310

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a1a1cbfef79'
down_revision = '3abaedd445a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('body', sa.Integer(), nullable=True))
    op.add_column('blogs', sa.Column('title', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_blogs_body'), 'blogs', ['body'], unique=False)
    op.create_index(op.f('ix_blogs_title'), 'blogs', ['title'], unique=False)
    op.drop_column('blogs', 'blog_body')
    op.drop_column('blogs', 'blog_title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('blog_title', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('blogs', sa.Column('blog_body', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_blogs_title'), table_name='blogs')
    op.drop_index(op.f('ix_blogs_body'), table_name='blogs')
    op.drop_column('blogs', 'title')
    op.drop_column('blogs', 'body')
    # ### end Alembic commands ###
