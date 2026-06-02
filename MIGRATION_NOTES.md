# Migration Notes — odoo-tmc-auditors (14.0 → 19.0)

Repo contains one module: `auditors`.

## Summary of changes by category

### Models

- No changes required. `auditors/models/institution.py`, `auditors/models/partner.py`,
  and `auditors/models/year.py` all use the modern API (`fields.*`, plain
  `models.Model`). No `name_get`, `fields_view_get`, `@api.one/@api.multi`,
  `read_group`, `_sql_constraints`, `track_visibility`, `xmlid_to_res_id`,
  `_cr/_uid/_context`, or single-record `create` overrides were found. None of the
  models inherit `tmc.category`, so no `_compute_display_name` porting was needed.

### Views

- `auditors/views/partner_views.xml`:
  - `<tree>` → `<list>` (17.0 rename). Record xmlid `partner_view_tree` kept unchanged.
  - `<field name="view_mode">tree,form</field>` → `list,form`.
  - Three `attrs` conversions (removed in 17.0) — all single-tuple, see below.
  - The `company_type` `position="attributes"` block set
    `<attribute name="attrs">{'invisible': True}</attribute>`; converted to
    `<attribute name="invisible">True</attribute>` (the field is unconditionally
    hidden).
- `auditors/views/institution_views.xml`:
  - `<tree>` → `<list>`; `view_mode` `tree,form` → `list,form`. Record xmlid
    `institution_view_tree` kept unchanged.
- Menus (`auditors_menus.xml`, `institution_menus.xml`): no changes. The `groups="..."`
  shortcut attribute on `<menuitem>` is unchanged in 19.0 (left as-is per spec).

### Security

- `auditors/security/auditors_groups.xml`: contains two `res.groups` records
  (`group_user`, `group_manager`) each with
  `<field name="category_id" ref="module_category_auditors"/>`. Per the spec security
  section, `category_id` on `res.groups` may need to become a 19.0 `privilege_id`. This
  is a non-trivial change and was NOT guessed. Left as-is and flagged under "Items left
  for human review".
- `ir.model.access.csv`: unchanged (CSV columns are unchanged in 19.0).
- No `groups_id` fields present on any affected model record (none to rename to
  `group_ids`).

### Tests

- None present.

### Manifests

- `auditors/__manifest__.py`: version `14.0.1.0.0` → `19.0.1.0.0`; added the missing
  `"installable": True` key. License already `AGPL-3`. No dead `"qweb": []` key was
  present. `depends` (`tmc`, `partner_tmc`, `partner_fiscal`) verified correct and kept
  unchanged. Data load order verified: security (groups → access csv) loads before
  views, and views load before the menus that reference their actions.

## 18.0 branch

- None existed. Branch `19.0` created fresh from `14.0`.

## Removed dependencies

- None removed.

## Dependencies to verify before push

- `tmc` — private TMC module; verify a 19.0 version is available in the addons path.
- `partner_tmc`, `partner_fiscal` — provided by the odoo-partner repo (already migrated
  to 19.0 in this workspace); verify both are installable at 19.0.

## attrs conversions to review

All three conversions used the identical single-tuple domain
`{'invisible': [('auditor', '=', False)]}`, which maps to `invisible="not auditor"`
(`auditor` is a Boolean field; `= False` is the falsy/negation case). None are compound
domains, so they are listed here only for completeness:

- `partner_views.xml` group `auditor_years`:
  `attrs="{'invisible':[('auditor','=',False)]}"` → `invisible="not auditor"`
- `partner_views.xml` field `year_ids`: `attrs="{'invisible':[('auditor','=',False)]}"`
  → `invisible="not auditor"`
- `partner_views.xml` page `resume`: `attrs="{'invisible':[('auditor','=',False)]}"` →
  `invisible="not auditor"`
- `partner_views.xml` field `company_type` (attribute-set form):
  `<attribute name="attrs">{'invisible': True}</attribute>` →
  `<attribute name="invisible">True</attribute>`

## Autosave / onchange → constrains conversions

- None. The repo has no `@api.onchange` methods.

## Items left for human review

- `auditors/security/auditors_groups.xml`: both `res.groups` records set
  `<field name="category_id" ref="module_category_auditors"/>`. In 19.0 group
  categorization may require a `privilege_id` instead of `category_id`. This was
  intentionally NOT changed to avoid guessing a privilege record. Review and adapt to
  the correct 19.0 form if needed.

## Lint findings

pre-commit ran fully (ruff, ruff-format, prettier with plugin-xml, check-xml,
pylint-odoo, odoo-pre-commit-hooks). Auto-fixers (ruff-format, prettier) reformatted the
XML views, the menus/security XML, the manifest, and these notes. Remaining reporter
findings (non-blocking, follow-ups):

- `manifest-required-author` (`auditors/__manifest__.py`): pylint-odoo's OCA rcfile
  requires the author "Odoo Community Association (OCA)". This is a private TMC module,
  not an OCA addon — expected and intentionally not changed.
- `missing-readme` (`auditors`): no `README.rst`. OCA convention; not added (out of
  scope for a static migration).
- The `.pylintrc` emits `unknown-option-value` warnings for several OCA-specific check
  names not recognized by the installed pylint core; these come from the shared tooling
  rcfile, not from this module's code.

## Translations

- Translation regeneration deferred to a later stage. </content> </invoke>
