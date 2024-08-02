/** @odoo-module */
import { registry } from '@web/core/registry';
import { listView } from '@web/views/list/list_view';
import { ListController } from '@web/views/list/list_controller';
import { WarningDialog } from "@web/core/errors/error_dialogs";
import { useService } from "@web/core/utils/hooks";
import { _t } from "@web/core/l10n/translation";

export class PopupController extends ListController {
    static template = "custom_new_module_form.ListView";
    setup() {
        super.setup();
        this.dialog = useService("dialog");
    }
    OnPopupClick() {
        this.dialog.add(WarningDialog, {
            title: _t("Message"),
            message: _t("Hello World"),
        });
    }
}

registry.category('views').add('button_in_tree', {
    ...listView,
    Controller: PopupController,
});