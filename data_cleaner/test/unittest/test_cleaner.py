import pytest
from mock import create_autospec
from data_cleaner.cleaning.cleaner import get_cleaned_file


def test_get_cleaned_df():
    mock_get_cleaned_file = create_autospec(get_cleaned_file, return_value='some cleaned pd_df')
    assert mock_get_cleaned_file(path='path', 
                               capitalize_list='capitalize_list',
                               numeric_list='numeric_list',
                               email_list='email_list',
                               partners_list='partners_list',
                               drop_empty_list='drop_empty_list' == 'some cleaned pd_df')

    mock_get_cleaned_file.assert_called_with(path='path', 
                               capitalize_list='capitalize_list',
                               numeric_list='numeric_list',
                               email_list='email_list',
                               partners_list='partners_list',
                               drop_empty_list='drop_empty_list' == 'some cleaned pd_df')