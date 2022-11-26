import pytest

import genshin


async def test_record_cards(client: genshin.Client, hoyolab_id: int):
    data = await client.get_record_cards(hoyolab_id)

    assert data

    assert data[0].level >= 40


async def test_genshin_user(client: genshin.Client, genshin_uid: int):
    data = await client.get_genshin_user(genshin_uid)

    assert data


async def test_partial_genshin_user(client: genshin.Client, genshin_uid: int):
    data = await client.get_partial_genshin_user(genshin_uid)

    assert data


async def test_spiral_abyss(client: genshin.Client, genshin_uid: int):
    data = await client.get_spiral_abyss(genshin_uid, previous=True)

    assert data


async def test_notes(lclient: genshin.Client, genshin_uid: int):
    data = await lclient.get_notes(genshin_uid)

    assert data

    if td := data.remaining_transformer_recovery_time:
        assert sum(1 for i in (td.days, td.hours, td.minutes, td.seconds) if i) == 1


async def test_genshin_activities(client: genshin.Client, genshin_uid: int):
    data = await client.get_activities(genshin_uid)

    assert data


async def test_full_genshin_user(client: genshin.Client, genshin_uid: int):
    data = await client.get_full_genshin_user(genshin_uid)

    assert data


async def test_exceptions(client: genshin.Client):
    with pytest.raises(genshin.DataNotPublic):
        await client.get_record_cards(10000000)

    with pytest.raises(genshin.AccountNotFound):
        await client.get_spiral_abyss(70000001)
