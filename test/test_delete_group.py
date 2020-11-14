from random import randrange


def test_add_group(app):
    if len(app.groups.get_group_list()) == 0:
        app.groups.add_new_group("my group")
    old_list = app.groups.get_group_list()
    print(old_list)
    index = randrange(1, len(old_list))
    app.groups.delete_group(index)
    new_list = app.groups.get_group_list()
    assert len(old_list) - 1 == len(new_list)
    old_list.remove(old_list[index])
    assert sorted(old_list) == sorted(new_list)
