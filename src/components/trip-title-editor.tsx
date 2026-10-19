"use client";

import { useState } from "react";

type Props = {
  initialTitle: string;
};

export default function TripTitleEditor({ initialTitle }: Props) {
  const [title, setTitle] = useState(initialTitle);
  const [draftTitle, setDraftTitle] = useState(initialTitle);
  const [isEditing, setIsEditing] = useState(false);
  const [error, setError] = useState("");

  function handleEdit() {
    // 每次开始编辑，都从当前已确认的标题创建草稿。
    setDraftTitle(title);
    setError("");
    setIsEditing(true);
  }

  function handleConfirm() {
    const nextTitle = draftTitle.trim();

    if (!nextTitle) {
      setError("请输入行程标题");
      return;
    }

    setTitle(nextTitle);
    setError("");
    setIsEditing(false);
  }

  function handleCancel() {
    setDraftTitle(title);
    setError("");
    setIsEditing(false);
  }

  return (
    <div>
      <h1>{title}</h1>

      {isEditing ? (
        <div>
          <label>
            行程标题：
            <input
              value={draftTitle}
              onChange={(event) => {
                setDraftTitle(event.target.value);
                setError("");
              }}
              aria-invalid={Boolean(error)}
              aria-describedby={error ? "title-error" : undefined}
            />
          </label>

          {error && (
            <p id="title-error" role="alert">
              {error}
            </p>
          )}

          <button type="button" onClick={handleConfirm}>
            确认
          </button>
          <button type="button" onClick={handleCancel}>
            取消
          </button>
        </div>
      ) : (
        <button type="button" onClick={handleEdit}>
          编辑标题
        </button>
      )}
    </div>
  );
}