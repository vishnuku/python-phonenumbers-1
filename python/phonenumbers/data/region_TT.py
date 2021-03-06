"""Auto-generated file, do not edit by hand. TT metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_TT = PhoneMetadata(id='TT', country_code=1, international_prefix='011',
    general_desc=PhoneNumberDesc(national_number_pattern='[589]\\d{9}', possible_number_pattern='\\d{7}(?:\\d{3})?', possible_length=(10,), possible_length_local_only=(7,)),
    fixed_line=PhoneNumberDesc(national_number_pattern='868(?:2(?:01|[23]\\d)|6(?:0[79]|1[02-8]|2[1-9]|[3-69]\\d|7[0-79])|82[124])\\d{4}', example_number='8682211234', possible_length=(10,), possible_length_local_only=(7,)),
    mobile=PhoneNumberDesc(national_number_pattern='868(?:2(?:6[6-9]|[789]\\d)|3(?:0[1-9]|1[02-9]|[2-9]\\d)|4[6-9]\\d|6(?:20|78|8\\d)|7(?:0[1-9]|1[02-9]|[2-9]\\d))\\d{4}', example_number='8682911234', possible_length=(10,), possible_length_local_only=(7,)),
    toll_free=PhoneNumberDesc(national_number_pattern='8(?:00|44|55|66|77|88)[2-9]\\d{6}', possible_number_pattern='\\d{10}', example_number='8002345678', possible_length=(10,)),
    premium_rate=PhoneNumberDesc(national_number_pattern='900[2-9]\\d{6}', possible_number_pattern='\\d{10}', example_number='9002345678', possible_length=(10,)),
    shared_cost=PhoneNumberDesc(),
    personal_number=PhoneNumberDesc(national_number_pattern='5(?:00|22|33|44|66|77|88)[2-9]\\d{6}', possible_number_pattern='\\d{10}', example_number='5002345678', possible_length=(10,)),
    voip=PhoneNumberDesc(),
    pager=PhoneNumberDesc(),
    uan=PhoneNumberDesc(),
    voicemail=PhoneNumberDesc(national_number_pattern='868619\\d{4}', possible_number_pattern='\\d{10}', example_number='8686191234', possible_length=(10,), possible_length_local_only=(7,)),
    no_international_dialling=PhoneNumberDesc(),
    national_prefix='1',
    national_prefix_for_parsing='1',
    leading_digits='868')
