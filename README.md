`echo /private$(getconf DARWIN_USER_DIR)com.apple.dock.launchpad/db/db`

## Fields explanation

| Field | Description |
| --- | --- |
| `apps::title` | APP Title |
| `apps::bundleid` | APP Bundle ID |
| `apps::item_id` == `items::rowid` -> `items::uuid` | APP UUID |
| `apps::item_id` == `items::rowid` -> `items::type` == `app_sources::rowid` -> `app_sources::uuid` | Source Type |
| `apps::category_id` == `categories::rowid` -> `categories::uti` | Category |
| `apps::item_id` == `items::rowid` -> `items::parent_id` == `groups::item_id` -> `groups::title` | Folder Title |
| `apps::moddate` |  |
| `apps::item_id` == `items::rowid` -> `items::ordering` | Index on Page |

| `app_sources::rowid` | UUID | Description |
| --- | --- | --- |
| 1 | read only | ROOTPAGE/ROOTPAGE_VERS |
| 2 | system | unknown |
| 3 | cryptexes | folders |
| 4 | user | user apps |
| 5 | shared users | shared user apps |
| 6 | internal | unknown |

| `items::flags` `app_sources::flags` | Description |
| --- | --- |
| null | System |
| 0 | Displayed |
| 1 |  |
| 2 |  |
| 4 |  |
| 5 | Emby/Outlook |
| 8 | Gray Icon |
| 13 |  |
| 40 | Hidden |
| 56 |  |
| 128 |  |

## Fields in tables

### apps
| Field | Type | Description |
| --- | --- | --- |
| item_id | INTEGER | APP ID |
| title | TEXT | APP Title |
| bundleid | TEXT | Bundle ID |
| storeid | INTEGER |  |
| category_id | INTEGER | Category ID |
| moddate | REAL |  |
| bookmark | BLOB |  |

### app_sources
| Field | Type | Description |
| --- | --- | --- |
| rowid | INTEGER | Source ID |
| uuid | TEXT | Source Type |
| flags | INTEGER |  |
| bookmark | BLOB |  |
| last_fsevent_id | INTEGER |  |
| fsevent_uuid | TEXT |  |

### categories
| Field | Type | Description |
| --- | --- | --- |
| rowid | INTEGER | Category ID |
| uti | TEXT | Category |

### groups
| Field | Type | Description |
| --- | --- | --- |
| item_id | INTEGER | Group ID |
| category_id | INTEGER | Category ID |
| title | TEXT | Folder Title |

### items
| Field | Type | Description |
| --- | --- | --- |
| rowid | INTEGER | APP ID |
| uuid | TEXT | APP UUID |
| flags | INTEGER |  |
| type | INTEGER | Source ID |
| parent_id | INTEGER | Group ID |
| ordering | INTEGER | Index on Page |
