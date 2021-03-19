import json

with open('/YearDataJSON/2021.json') as f:
    data = json.load(f)

import sys

for week in data:
    playlist = week['playlist']
    date = week['date']
    description = week['description']

    dd = f"""
        <div
      class="fl-module fl-module-rich-text fl-node-60095f7898484 fl-editable fl-editable-focused"
      data-node="60095f7898484"
      data-parent="6009533b1e79d"
      data-type="rich-text"
      data-name="Text Editor"
    >
      <div class="fl-module-content fl-node-content">
        <div
          class="fl-rich-text mce-content-body mce-edit-focus"
          id="mce_19"
          contenteditable="true"
          style="position: relative"
          spellcheck="false"
        >
          <p><strong>{date}</strong></p>
          <p>
            {description}
          </p>
        </div>
      </div>

      <div
        id="fl-inline-editor-60095f7898484"
        class="fl-inline-editor"
        style="display: none"
      >
        <div
          id="mceu_74"
          class="mce-tinymce mce-tinymce-inline mce-container mce-panel fl-inline-editor-active-toolbar"
          hidefocus="1"
          tabindex="-1"
          role="application"
          style="border-width: 1px; left: 0px; top: 0px; width: 0px; height: 0px"
        >
          <div
            id="mceu_74-body"
            class="mce-container-body mce-abs-layout"
            style="width: 0px; height: 0px"
          >
            <div id="mceu_74-absend" class="mce-abs-end"></div>
            <div
              id="mceu_75"
              class="mce-toolbar-grp mce-container mce-panel mce-abs-layout-item mce-first mce-last"
              hidefocus="1"
              tabindex="-1"
              role="group"
              style="left: 0px; top: 0px; width: 0px; height: 0px"
            >
              <div
                id="mceu_75-body"
                class="mce-container-body mce-stack-layout"
                style="width: 0px; height: 0px"
              >
                <div
                  id="mceu_76"
                  class="mce-container mce-toolbar mce-stack-layout-item mce-first mce-last"
                  role="toolbar"
                >
                  <div id="mceu_76-body" class="mce-container-body mce-flow-layout">
                    <div
                      id="mceu_77"
                      class="mce-container mce-flow-layout-item mce-first mce-btn-group"
                      role="group"
                    >
                      <div id="mceu_77-body">
                        <div
                          id="mceu_66"
                          class="mce-widget mce-btn mce-first mce-active"
                          tabindex="-1"
                          aria-pressed="true"
                          role="button"
                          aria-label="Bold"
                        >
                          <button
                            id="mceu_66-button"
                            role="presentation"
                            type="button"
                            tabindex="-1"
                          >
                            <i class="mce-ico mce-i-bold"></i>
                          </button>
                        </div>
                        <div
                          id="mceu_67"
                          class="mce-widget mce-btn"
                          tabindex="-1"
                          aria-pressed="false"
                          role="button"
                          aria-label="Italic"
                        >
                          <button
                            id="mceu_67-button"
                            role="presentation"
                            type="button"
                            tabindex="-1"
                          >
                            <i class="mce-ico mce-i-italic"></i>
                          </button>
                        </div>
                        <div
                          id="mceu_68"
                          class="mce-widget mce-btn"
                          tabindex="-1"
                          aria-pressed="false"
                          role="button"
                          aria-label="Strikethrough"
                        >
                          <button
                            id="mceu_68-button"
                            role="presentation"
                            type="button"
                            tabindex="-1"
                          >
                            <i class="mce-ico mce-i-strikethrough"></i>
                          </button>
                        </div>
                        <div
                          id="mceu_69"
                          class="mce-widget mce-btn"
                          tabindex="-1"
                          aria-pressed="false"
                          role="button"
                          aria-label="Insert/edit link"
                        >
                          <button
                            id="mceu_69-button"
                            role="presentation"
                            type="button"
                            tabindex="-1"
                          >
                            <i class="mce-ico mce-i-link"></i>
                          </button>
                        </div>
                        <div
                          id="mceu_70"
                          class="mce-widget mce-btn mce-last"
                          tabindex="-1"
                          aria-pressed="false"
                          role="button"
                          aria-label="Underline"
                        >
                          <button
                            id="mceu_70-button"
                            role="presentation"
                            type="button"
                            tabindex="-1"
                          >
                            <i class="mce-ico mce-i-underline"></i>
                          </button>
                        </div>
                      </div>
                    </div>
                    <div
                      id="mceu_78"
                      class="mce-container mce-flow-layout-item mce-last mce-btn-group"
                      role="group"
                    >
                      <div id="mceu_78-body">
                        <div
                          id="mceu_71"
                          class="mce-widget mce-btn mce-first"
                          tabindex="-1"
                          aria-pressed="false"
                          role="button"
                          aria-label="Align left"
                        >
                          <button
                            id="mceu_71-button"
                            role="presentation"
                            type="button"
                            tabindex="-1"
                          >
                            <i class="mce-ico mce-i-alignleft"></i>
                          </button>
                        </div>
                        <div
                          id="mceu_72"
                          class="mce-widget mce-btn"
                          tabindex="-1"
                          aria-pressed="false"
                          role="button"
                          aria-label="Align centre"
                        >
                          <button
                            id="mceu_72-button"
                            role="presentation"
                            type="button"
                            tabindex="-1"
                          >
                            <i class="mce-ico mce-i-aligncenter"></i>
                          </button>
                        </div>
                        <div
                          id="mceu_73"
                          class="mce-widget mce-btn mce-last"
                          tabindex="-1"
                          aria-pressed="false"
                          role="button"
                          aria-label="Align right"
                        >
                          <button
                            id="mceu_73-button"
                            role="presentation"
                            type="button"
                            tabindex="-1"
                          >
                            <i class="mce-ico mce-i-alignright"></i>
                          </button>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    """

    print(dd)

    row = 1
    trs = []
    trstring = ""
    for song in playlist:
        if (row % 2) == 0:
            # Even
            tr = f"""
            <tr class="pp-table-row even">
                <td>
                    <b class="tablesaw-cell-label">Composer</b>
                    <span class="tablesaw-cell-content">{song['composer']}<span>
                </td>
                <td>
                    <b class="tablesaw-cell-label">Work</b>
                    <span class="tablesaw-cell-content">{song['work']}</span>
                </td>
                <td>
                    <b class="tablesaw-cell-label">Performers</b>
                    <span class="tablesaw-cell-content">{song['performers']}</span>
                </td>
                <td>
                    <b class="tablesaw-cell-label">label</b>
                    <span class="tablesaw-cell-content">{song['label']}</span>
                </td>
                <td>
                    <b class="tablesaw-cell-label">Air Time</b>
                    <span class="tablesaw-cell-content">{song['air time']}</span>
                </td>
            </tr>
            """
        else:
            # Odd
            tr = f"""
            <tr class="pp-table-row odd">
                <td>
                    <b class="tablesaw-cell-label">Composer</b>
                    <span class="tablesaw-cell-content">{song['composer']}<span>
                </td>
                <td>
                    <b class="tablesaw-cell-label">Work</b>
                    <span class="tablesaw-cell-content">{song['work']}</span>
                </td>
                <td>
                    <b class="tablesaw-cell-label">Performers</b>
                    <span class="tablesaw-cell-content">{song['performers']}</span>
                </td>
                <td>
                    <b class="tablesaw-cell-label">label</b>
                    <span class="tablesaw-cell-content">{song['label']}</span>
                </td>
                <td>
                    <b class="tablesaw-cell-label">Air Time</b>
                    <span class="tablesaw-cell-content">{song['air time']}</span>
                </td>
            </tr>
            """
        trs.append(tr)
        row += 1

    for xtr in trs:
        trstring = trstring + " " + str(xtr)
    fulltablestr = f"""
                    <div
  class="fl-module fl-module-pp-table fl-node-6009533b1e4de tb"
  data-node="6009533b1e4de"
  data-parent="6009533b1e79d"
  data-type="pp-table"
  data-name="Table"
>
  <div class="fl-module-content fl-node-content">
    <div class="pp-table-wrap">
      <div class="tablesaw-bar mode-stack"></div>
      <table
        class="pp-table-6009533b1e4de pp-table-content tablesaw tablesaw-stack"
        data-tablesaw-mode="stack"
        data-tablesaw-minimap=""
        id="table-5842"
      >
        <thead>
          <tr>
            <th
              id="pp-table-col-1"
              class="pp-table-col"
              scope="col"
              data-tablesaw-sortable-col=""
            >
              Composer
            </th>
            <th
              id="pp-table-col-2"
              class="pp-table-col"
              scope="col"
              data-tablesaw-sortable-col=""
            >
              Work
            </th>
            <th
              id="pp-table-col-3"
              class="pp-table-col"
              scope="col"
              data-tablesaw-sortable-col=""
            >
              Performers
            </th>
            <th
              id="pp-table-col-4"
              class="pp-table-col"
              scope="col"
              data-tablesaw-sortable-col=""
            >
              label
            </th>
            <th
              id="pp-table-col-5"
              class="pp-table-col"
              scope="col"
              data-tablesaw-sortable-col=""
            >
              Air Time
            </th>
          </tr>
        </thead>
        <tbody>
        {trstring}
        </tbody>
      </table>
    </div>
  </div>
</div>
    """
    print(fulltablestr)
    sys.exit()
