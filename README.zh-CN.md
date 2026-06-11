<div align="center">

# Human Kernel

**你的一切，构成一个归你所有的内核。**

<p>
  <a href="https://humankernel.org">官网</a> ·
  <a href="#三层结构">工作原理</a> ·
  <a href="https://github.com/human-kernel/human-kernel/discussions">讨论区</a> ·
  <a href="#参与贡献">参与贡献</a>
</p>

<p>
  <a href="./LICENSE"><img alt="License: AGPL-3.0" src="https://img.shields.io/github/license/human-kernel/human-kernel?color=blue"></a>
  <a href="https://github.com/human-kernel/human-kernel/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/human-kernel/human-kernel?style=flat&logo=github&color=yellow"></a>
  <a href="https://github.com/human-kernel/human-kernel/commits/main"><img alt="Commit activity" src="https://img.shields.io/github/commit-activity/m/human-kernel/human-kernel?color=green"></a>
  <a href="https://github.com/human-kernel/human-kernel/issues"><img alt="Issues" src="https://img.shields.io/github/issues/human-kernel/human-kernel"></a>
  <a href="https://github.com/human-kernel/human-kernel/discussions"><img alt="Discussions" src="https://img.shields.io/github/discussions/human-kernel/human-kernel?color=purple"></a>
  <img alt="PRs welcome" src="https://img.shields.io/badge/PRs-welcome-brightgreen">
  <img alt="Status: early" src="https://img.shields.io/badge/status-early%20%26%20unstable-orange">
</p>

<p>
  <a href="./README.md"><img alt="README in English" src="https://img.shields.io/badge/English-d9d9d9"></a>
  <a href="./README.zh-CN.md"><img alt="简体中文版 README" src="https://img.shields.io/badge/简体中文-d9d9d9"></a>
  <img alt="Your language" src="https://img.shields.io/badge/%E4%BD%A0%E7%9A%84%E8%AF%AD%E8%A8%80%20%E2%86%92%20PR-ffd9d9">
</p>

</div>

---

> **你的一切，构成一个归你所有的内核。**
> **你的另一面从中生长——与你共生，在数字世界里主动流动，有时先你一步。**
> **由你构成，归你所有，与你同行。**

Human Kernel 是一个开源协议与本地优先应用，用于为一个人建模——身份、价值观、关系、知识、经历、偏好、能力与授权边界——让你授权的 agent 能够理解你，并作为你的另一面行动。

Agent 越来越能干，但它们并不真正知道**自己在为谁行动**。今天，「关于你」的知识散落在聊天记录和平台拥有的封闭记忆功能里。Human Kernel 选择相反的立场：关于你的模型应该是一等造物——结构化、可审视、可纠正——并且归你所有。

## 三层结构

| 层 | 是什么 | 你控制什么 |
| --- | --- | --- |
| **内核（kernel）** | 一个结构化、证据支撑的个人模型。其中每一条判断都能回答：*你为什么这么认为？证据来自哪里？现在还成立吗？我能改吗？* | 存储在本地，完全归你。 |
| **另一面（alter ego）** | 从内核中生长出的表达层：像你一样回答、推理、提醒、准备、行动——不是「挂上你的数据的通用助手」。 | 只在你授予的权限内行动。 |
| **Human API** | 一个有权限边界的调用面，让其他人、产品和 agent 可以查询或调用你的某个切片。 | 哪些切片存在、谁能调用、什么需要确认，都由你决定。 |

## 原则

- **本地优先。** 内核的权威数据在你的设备上，不在任何人的服务器上。
- **证据优先。** 关于你的论断必须能回溯到来源。判断带有置信度，会过期、可质疑、可纠正——纠正会向下传播。
- **你是编辑。** 「这不对」「这过时了」「这是真的，但永远别用」都是一等操作。
- **行动保守。** 沉默是一种正当的行动。alter ego 在权限之外先问后做；任何离开你设备的数据都有审计记录。
- **不宣称灵魂。** 内核从不宣称知道「真实的你」。它持有的是有证据、可纠正的假设：你在乎什么，你如何权衡。
- **开放协议。** schema、协议与应用全部开源——要求用户交出如此多的信任，封闭黑箱不是一个合理的要求。

## 这不是什么

- ❌ 不是项目管理或任务工具。执行系统可以作为后端接入，但它们不是产品本身。
- ❌ 不是笔记应用、记忆数据库或「第二大脑」浏览器。
- ❌ 不是 AI 伴侣，也不是性格测试。它不给你打分、不给你分型、不下诊断。
- ❌ 不是托管你人生的云服务。不存在服务端母本。

## 路线图

- [ ] **协议 spec v0.1** —— 内核的结构：证据、判断、纠正、权限
- [ ] **参考应用** —— 实现 spec 的本地优先应用
- [ ] **Human API 草案** —— 对内核切片的有权限查询
- [ ] **Agent runtime 集成** —— 把授权后的行动交给执行后端

进展与讨论见[讨论区](https://github.com/human-kernel/human-kernel/discussions)。早期且不稳定，公开开发中。会有破坏性变更；暂时不要在其上构建。

## 用你的语言写下宣言

内核属于所有人，所以宣言应该存在于所有语言中。

| 语言 | 宣言 |
| --- | --- |
| English | [README.md](./README.md) |
| 中文 | 见上 |
| *你的语言？* | *把三行宣言翻译成你的母语，是这个项目最小、也最受欢迎的首次贡献——欢迎提 PR* |

## 参与贡献

项目当前阶段最有价值的贡献是**尖锐的问题**和**宣言翻译**。

1. **反驳我们** —— 在[讨论区](https://github.com/human-kernel/human-kernel/discussions)对协议方向提出异议
2. **翻译宣言** —— 把你的语言加进上面的表格
3. **Watch 本仓库** —— spec v0.1 会首先在这里落地

## Star History

<a href="https://star-history.com/#human-kernel/human-kernel&Date">
  <img src="https://api.star-history.com/svg?repos=human-kernel/human-kernel&type=Date" alt="Star History Chart" width="600">
</a>

## 许可

[AGPL-3.0](./LICENSE)。你的内核归你；处理它的代码保持开放——包括有人把它作为服务运行时。
