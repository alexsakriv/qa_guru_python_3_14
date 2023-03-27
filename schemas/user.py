from voluptuous import PREVENT_EXTRA, Schema


user = Schema(
    {
        "id": int,
        "email": str,
        "first_name": str,
        "last_name": str,
        "avatar": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

support = Schema(
    {
        "url": str,
        "text": str,
    },
    extra=PREVENT_EXTRA,
    required=True
)

single_user_schema = Schema(
    {
        "data": user,
        "support": support,
    },
    extra=PREVENT_EXTRA,
    required=True
)