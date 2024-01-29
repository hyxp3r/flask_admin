from flask_admin.contrib.sqla import ModelView


class IndividualView(ModelView):
    can_edit = True
    can_create = True
    can_delete = True
    can_view_details = True

    column_sortable_list = ['created_at']

    form_columns = ['title', 'short_title']

    #edit_template = 'individual_edit.html'
