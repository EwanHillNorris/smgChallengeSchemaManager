def is_compatible(change_report):
    return (
        not change_report["removed_fields"]
        and not change_report["type_changes"]
    )
