import random


def test_add_group(app):
    if len(app.groups.get_group_list()) == 0:
        app.groups.add_new_group("my group")
    old_list = app.groups.get_group_list()
    print(old_list)
    group = random.choice(old_list)
    index = old_list.index(group)
    print(group)
    app.groups.delete_group(index)
    new_list = app.groups.get_group_list()
    assert len(old_list) - 1 == len(new_list)
    old_list.remove(old_list[index])
    assert sorted(old_list) == sorted(new_list)