from formfactory import actions


@actions.register
def dummy_action(form_instance):
    return True

