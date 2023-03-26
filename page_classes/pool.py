from base.commonmethods import CommonMethods
import random
import time


class PoolPage(CommonMethods):

    def __init__(self, driver):
        self.driver = driver

# == Pool Page Locators ================================================================================================

    _pool_configuration_table = 'your-locator'
    _create_thick_pool_button = 'your-locator'
    _create_thin_pool_button = 'your-locator1'
    _create_tier_pool_button = 'your-locator'
    _delete_button = 'your-locator'
    _extend_button = 'your-locator'
    _rename_button = 'your-locator'
    _show_properties_button = 'your-locator'
    _pool_creation_modal = 'your-locator'
    _pool_name_input = 'your-locator'
    _optimize_pool_for_dropdown_list = 'your-locator'
    _raid_mode_dropdown_list = 'your-locator'
    _disk_type_dropdown_list = 'your-locator'
    _stripe_size_dropdown_list = 'your-locator'
    _disk_number_dropdown_list = 'your-locator'
    _span_depth_dropdown_list = 'your-locator'
    _enable_cache_checkbox = 'your-locator'
    _pool_creation_create_button = 'your-locator'
    _pool_creation_cancel_button = 'your-locator'
    _automatically_radio_button = 'your-locator'
    _manually_radio_button = 'your-locator'
    _pool_creation_not_enough_disks_warning = 'your-locator'
    _pool_extension_not_enough_disks_warning = 'your-locator'
    _no_cache_slot_available_warning = 'your-locator'
    _confirm_delete_button = 'your-locator'
    _pool_creation_available_disks = 'your-locator'
    _pool_creation_invalid_name_warning = 'your-locator'
    _duplicate_name_warning = 'your-locator'
    _pool_rename_modal = 'your-locator'
    _new_name_input = 'your-locator'
    _pool_rename_button = 'your-locator'
    _delete_confirmation_message = 'your-locator'
    _disks_table = 'your-locator'
    _error_message = 'your-locator'
    _disks_table_pool_creation_extension_modal ='your-locator'
    _pool_extension_modal = 'your-locator'
    _extend_pool_button = 'your-locator'

# = Pool Page Methods ==================================================================================================

    def click_create_btn(self):
        self.wait_for_element(self._create_thick_pool_button)
        self.element_click(self._create_thick_pool_button, locatortype="id")
        self.wait_for_element(self._pool_creation_modal, wait_method='presence')

    def click_create_thin_btn(self):
        self.element_click(self._create_thin_pool_button, locatortype="id")

    def click_create_tier_pool_btn(self):
        self.element_click(self._create_tier_pool_button, locatortype="id")

    def click_delete_btn(self):
        self.wait_for_element(self._delete_button, locator_type="id")
        time.sleep(0.5)
        self.element_click(self._delete_button)
        self.wait_for_element(self._delete_confirmation_message, locator_type="xpath", wait_method='visible', timeout=5)

    def click_extend_btn(self):
        self.wait_for_element(self._extend_button, locator_type="id")
        self.element_click(self._extend_button, locatortype="id")
        self.wait_for_element(self._pool_extension_modal, locator_type="id", wait_method='visible', timeout=5)

    def click_rename_btn(self):
        self.wait_for_element(self._rename_button, locator_type="id")
        self.element_click(self._rename_button, locatortype="id")
        self.wait_for_element(self._pool_rename_modal, locator_type="xpath", wait_method='visible', timeout=5)

    def click_show_properties_btn(self):
        self.element_click(self._show_properties_button, locatortype="id")

    def check_pool_existence(self, pool_name):
        self.wait_for_element(self._pool_configuration_table, locator_type='xpath', wait_method='visible')
        pool = 'pool-xpath'
        assert self.element_presence_check(pool, by_type='xpath') == True,\
            'The storage Pool "' + pool_name + '" hasn\'t been created successfully,' \
            ' and it\'s not shown in Pool Configuration table.'

    def select_desired_pool(self, pool_name):
        self.wait_for_element(self._pool_configuration_table, locator_type='xpath', wait_method='visible')
        pool = 'pool-xpath'
        assert self.element_presence_check(pool, by_type='xpath') == True,\
            "Pool with name '" + pool_name + "' does\'nt exists in Pool Configuration table."
        self.element_click(pool, locatortype='xpath')
        try:
             self.element_click(pool, locatortype='xpath')
        except NoSuchElementException:
             pass
        else:
            raise AssertionError("Pool with name '" + pool_name + "' does\'nt exists in Pool Configuration table.")

# = Thick Pool Creation Methods ========================================================================================

    def enter_pool_name(self, pool_name):
        self.send_keys(pool_name, self._pool_name_input)

    def check_duplicate_name_warning(self):
        return self.element_presence_check(self._duplicate_name_warning, by_type='xpath')

    def select_optimize_pool_for(self, optimize_for):
        self.dropdown_by_text(optimize_for, self._optimize_pool_for_dropdown_list)

    def select_raid_mode(self, raid_mode):
        self.dropdown_by_text(raid_mode, self._raid_mode_dropdown_list)

    def select_disk_number(self, disk_num):
        self.dropdown_by_text(disk_num, self._disk_number_dropdown_list)

    def select_disk_type(self, disk_type):
        self.dropdown_by_text(disk_type, self._disk_type_dropdown_list)

    def click_automatically(self):
        self.element_click(self._automatically_radio_button)

    def click_manually(self):
        self.element_click(self._manually_radio_button)

    def enable_cache(self):
        self.element_click(self._enable_cache_checkbox)

    def click_create_pool_btn(self):
        self.element_click(self._pool_creation_create_button)
        self.wait_for_element(self._pool_creation_modal, wait_method='invisible', timeout=60)

    def check_disk_warning_pool_creation(self):
        disks_warning = self.element_is_displayed(self._pool_creation_not_enough_disks_warning, locator_type="xpath")
        assert disks_warning == False, 'There are not enough disks available to create storage Pool'

    def disk_selection(self, disk_number, select_method='manually'):
        self.wait_for_element(
            self._disks_table_pool_creation_extension_modal, locator_type="xpath", wait_method="presence")
        if select_method == "automatically":
            self.element_click(self._automatically_radio_button)
        else:
            self.element_click(self._manually_radio_button)
            disks = self.driver.find_elements_by_xpath(self._pool_creation_available_disks)
            selected_disks = random.sample(range(0, len(disks)), disk_number)
            for i in selected_disks:
                disks[i].click()

    def cache_settings(self, enable_cache):
        if enable_cache == "True":
            assert self.element_presence_check(self._no_cache_slot_available_warning, by_type='xpath') == False, \
                'There is no cache slot available'
            self.element_click(self._enable_cache_checkbox)

# = Delete Pool Methods ================================================================================================

    def confirm_delete_pool(self):
        self.wait_for_element(self._delete_confirmation_message, locator_type="xpath", wait_method="visible")
        self.element_click(self._confirm_delete_button, locatortype="id")
        self.wait_for_element(
            self._delete_confirmation_message, locator_type='xpath',wait_method='invisible', timeout=30)

    def verify_pool_deletion(self, pool_name):
        self.wait_for_element(self._pool_configuration_table, locator_type='xpath', wait_method='visible')
        pool = 'pool-xpath'
        assert self.element_presence_check(pool, by_type='xpath') == False, \
            'The storage Pool "' + pool_name + '" hasn\'t been deleted successfully,' \
                                               ' and it\'s shown in Pool Configuration table.'

# = Rename Pool Methods ================================================================================================

    def enter_pool_new_name(self, pool_new_name):
        self.send_keys(pool_new_name, self._new_name_input)

    def click_rename(self):
        self.element_click(self._pool_rename_button)
        self.wait_for_element(self._pool_rename_modal, locator_type="xpath", wait_method="invisible", timeout=20)

# = Pool Extension Methods =============================================================================================

    def click_extend_pool_btn(self):
        self.element_click(self._extend_pool_button)
        self.wait_for_element(self._pool_extension_modal, locator_type="id", wait_method="invisible", timeout=60)

    def check_disk_warning_pool_extension(self):
        disks_warning = self.element_is_displayed(self._pool_extension_not_enough_disks_warning, locator_type="xpath")
        assert disks_warning == False, 'There are not enough disks available to extend storage Pool'

