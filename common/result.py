def gen_result_format(status=0, message="", **kwargs):
    result = {
        "status": status,
        "message": message
    }
    result.update(kwargs)
    return result
