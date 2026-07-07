(function () {
  const text = {
    zh: {
      microstepLabels: {
        0: "000：15 rpm",
        2: "001：7.5 rpm",
        4: "010：未定义 / 保留",
        6: "011：3.75 rpm",
        8: "100：0.94 rpm",
        10: "101：0.47 rpm",
        12: "110：未定义 / 保留",
        14: "111：未定义 / 保留",
      },
      invalid: "请输入 0~255 的十进制值。",
      reserved: "当前 M2M1M0 编码未在上传文档中定义，使用前请确认固件说明。",
      ready: "可将十进制结果写入地址 18 / 0x12。",
      direction: "BIT0 驱动方向",
      forward: "正向",
      reverse: "反向",
      step: "BIT3~BIT1 步数",
      speedMode: "BIT4 速度模式",
      speedStop: "速度 0 表示停止",
      speedMax: "速度 0 表示最高速度",
      limitPhase: "BIT5 限位 / 零点相位",
      lowActive: "0 电平有效",
      highActive: "1 电平有效",
      currentPhase: "BIT6 目标电流相位",
      currentDefault: "目标电流 0 表示默认电流",
      currentZero: "目标电流 0 表示 0 电流",
      heartbeat: "BIT7 心跳功能",
      disabled: "关闭",
      enabled: "开启",
    },
    en: {
      microstepLabels: {
        0: "000: 15 rpm",
        2: "001: 7.5 rpm",
        4: "010: undefined / reserved",
        6: "011: 3.75 rpm",
        8: "100: 0.94 rpm",
        10: "101: 0.47 rpm",
        12: "110: undefined / reserved",
        14: "111: undefined / reserved",
      },
      invalid: "Enter a decimal value from 0 to 255.",
      reserved: "This M2M1M0 code is not defined in the supplied register table. Confirm your firmware before using it.",
      ready: "Write this decimal value to address 18 / 0x12.",
      direction: "BIT0 direction phase",
      forward: "forward",
      reverse: "reverse",
      step: "BIT3-BIT1 step code",
      speedMode: "BIT4 speed-mode behavior",
      speedStop: "speed 0 means stop",
      speedMax: "speed 0 means maximum speed",
      limitPhase: "BIT5 limit / home input phase",
      lowActive: "low level active",
      highActive: "high level active",
      currentPhase: "BIT6 target-current behavior",
      currentDefault: "target current 0 means default current",
      currentZero: "target current 0 means zero current",
      heartbeat: "BIT7 heartbeat",
      disabled: "disabled",
      enabled: "enabled",
    },
  };

  function localeFor(tool) {
    return tool.dataset.phaseLocale === "en" ? "en" : "zh";
  }

  function parsePhaseValue(raw) {
    const value = raw.trim();
    if (!value) return null;
    if (!/^\d+$/.test(value)) return Number.NaN;

    const parsed = Number.parseInt(value, 10);

    if (!Number.isInteger(parsed) || parsed < 0 || parsed > 255) {
      return Number.NaN;
    }

    return parsed;
  }

  function describe(value, locale) {
    const copy = text[locale];
    const microstepValue = value & 0x0e;
    return [
      `${copy.direction}: ${value & 0x01 ? copy.reverse : copy.forward}`,
      `${copy.step}: ${copy.microstepLabels[microstepValue]}`,
      `${copy.speedMode}: ${value & 0x10 ? copy.speedMax : copy.speedStop}`,
      `${copy.limitPhase}: ${value & 0x20 ? copy.highActive : copy.lowActive}`,
      `${copy.currentPhase}: ${value & 0x40 ? copy.currentZero : copy.currentDefault}`,
      `${copy.heartbeat}: ${value & 0x80 ? copy.enabled : copy.disabled}`,
    ];
  }

  function syncControls(tool, value) {
    tool.querySelectorAll("[data-phase-bit]").forEach((select) => {
      const bit = Number.parseInt(select.dataset.phaseBit, 10);
      select.value = value & (1 << bit) ? "1" : "0";
    });

    const microstep = tool.querySelector("[data-phase-microstep]");
    const microstepValue = value & 0x0e;
    if (microstep && Array.from(microstep.options).some((option) => Number(option.value) === microstepValue)) {
      microstep.value = String(microstepValue);
    }
  }

  function update(tool, value, options) {
    const locale = localeFor(tool);
    const copy = text[locale];
    const dec = tool.querySelector("[data-phase-dec]");
    const list = tool.querySelector("[data-phase-breakdown]");
    const message = tool.querySelector("[data-phase-message]");

    dec.textContent = String(value);

    list.replaceChildren(
      ...describe(value, locale).map((text) => {
        const item = document.createElement("li");
        item.textContent = text;
        return item;
      })
    );

    const microstepValue = value & 0x0e;
    if (message) {
      if (options && options.invalid) {
        message.textContent = copy.invalid;
      } else if ([4, 12, 14].includes(microstepValue)) {
        message.textContent = copy.reserved;
      } else {
        message.textContent = copy.ready;
      }
    }
  }

  function valueFromControls(tool) {
    let value = Number.parseInt(tool.querySelector("[data-phase-microstep]").value, 10);
    tool.querySelectorAll("[data-phase-bit]").forEach((select) => {
      if (select.value === "1") {
        value += 1 << Number.parseInt(select.dataset.phaseBit, 10);
      }
    });
    return value;
  }

  function initTool(tool) {
    const input = tool.querySelector("[data-phase-input]");

    tool.querySelectorAll("select").forEach((select) => {
      select.addEventListener("change", () => {
        const value = valueFromControls(tool);
        input.value = "";
        update(tool, value);
      });
    });

    input.addEventListener("input", () => {
      const parsed = parsePhaseValue(input.value);
      if (parsed === null) {
        update(tool, valueFromControls(tool));
        return;
      }
      if (Number.isNaN(parsed)) {
        update(tool, valueFromControls(tool), { invalid: true });
        return;
      }
      syncControls(tool, parsed);
      update(tool, parsed);
    });

    update(tool, valueFromControls(tool));
  }

  function init() {
    document.querySelectorAll("[data-ttlsd-phase-tool]").forEach(initTool);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
